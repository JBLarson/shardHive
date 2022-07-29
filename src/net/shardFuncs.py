#!/usr/bin/python3

import cryptography
from cryptography.fernet import Fernet
import json
import datetime
from time import strftime, strptime, sleep
import time
from secrets import *
import secrets
import paramiko
import pysftp
import os



def readJson(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict



global logDecryptedShard
logDecryptedShard = True


ioFile = "gData2.json"
theUserId = 16
gData = readJson(ioFile)
#gData = {"message": "testing shit yo"}



# input data classifier needs a lot of work.
# the goal is to make everything a string, JSON works well

if type(gData) == type(str):
	theUserPk = gData
else:
	theUserPk = str(gData)
#print(type(theUserPk))


# export data to json
def writeJson(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("Success Creating JSON at: " + str(jsonOutAddr))
	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)
	return functionOutput



# create time variables
timeRn = datetime.datetime.now()
dtRn1 = str(strftime("%x") + "_" + strftime("%X"))
dtRn0 = dtRn1.replace('/', '_')
dtRn = dtRn0.replace(':', '_')


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  

#don't delete anything without testing. who tf knows where dependencies be

def shardString(inputStr, numShards):

	strLen = len(inputStr)
	shardLen = strLen / numShards
	rangeList0 = []
	for shard in range((numShards+1)):
		shardRange = shard*shardLen
		rangeList0.append(shardRange)

	rangeList1 = []
	for sRange in rangeList0:
		sIndex = rangeList0.index(sRange)
		currentShardRange = rangeList0[sIndex]
		if sIndex > 0:
			lastShardRange = rangeList0[sIndex-1]

			rangePair = [int(lastShardRange), int(currentShardRange)]
			rangeList1.append(rangePair)

	shardList = []	
	for currentRange in rangeList1:
		currentShard = inputStr[currentRange[0]: currentRange[1]]
		shardList.append(currentShard)
	return shardList








def shardAndEncrypt(userId, pKey):

	# create user dir if it doesnt exist
	try:	os.system('mkdir ' + 'pr/' + str(userId) + '/')
	except Exception: pass

	# create user tmp dir
	try:	os.system('mkdir ' + 'pr/' + str(userId) + '/tmp')
	except Exception:	pass



	# need to test if userKey already exists so it isn't overwritten
	try:
		currentKeyAddr = ('pr/' + str(userId) + '.key')
		keyFile = open(currentKeyAddr, 'rb')
		currentKey = keyFile.read()
		#print('Success opening: ' + str(currentKeyAddr))
	except:

		currentKeyAddr = keyGen(userId)
		#print('\nFailed to open existing shardKey. Creating a new one')
		keyFile = open(currentKeyAddr, 'rb')
		currentKey = keyFile.read()
	
	keyFile.close()
	# end of key opening / creation


	pkShards = shardString(pKey, 8)
	#print(pkShards)


	# write unencrypted json in tmp dir

	shardDict = {}
	for shard in pkShards:
		shardIndex = str(pkShards.index(shard))
		jsonAddr = 'pr/' + str(userId) + '/tmp/' + str(shardIndex) + '.json'
		createCurrentJson = writeJson(jsonAddr, shard)

	# encrypt unencrypted shards
	for shard in pkShards:
		shardIndex = str(pkShards.index(shard))

		currentJsonAddr = 'pr/' + str(userId) + '/' + str(shardIndex) + '.json'
		currentTmpJsonAddr = 'pr/' + str(userId) + '/tmp/' + str(shardIndex) + '.json'

		with open(currentTmpJsonAddr, 'rb') as f:
			currentJson = f.read()

		fernet = Fernet(currentKey)
		encryptedJson = fernet.encrypt(currentJson)

		encryptedJsonAddr = str(currentJsonAddr) + '.encrypted'

		with open(encryptedJsonAddr, 'wb') as f:
			f.write(encryptedJson)

		shardDict.update({shardIndex: encryptedJsonAddr})

	# remove tmp dir
	try:	os.system('rm -rf ' + 'pr/' + str(userId) + '/tmp')
	except Exception:	pass


	return shardDict











def keyGen(keyName):
	key = Fernet.generate_key()
	keyAddr = 'pr/' + str(keyName) + '.key'
	file = open(keyAddr, 'wb')
	file.write(key)
	file.close()
	msg = '\nCreated key at: ' + str(keyAddr)
	#print(msg)
	return keyAddr





# from sftpWrite.py then createNetMap.py as of 7_29 it's distribute.py

def writeFile(ftpServerName, configUser, dataToWrite):
	cnopts, port = pysftp.CnOpts(), 22
	cnopts.hostkeys = None 
	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		#print('Success connecting to: ' +str(ftpServerName))

		try:
			conn.cwd('FTP/hive/' + str(configUser) + '/')
		except:
			conn.mkdir('FTP/hive/' + str(configUser) + '/')
			conn.cwd('FTP/hive/' + str(configUser) + '/')
		try:
			conn.put(dataToWrite)
			#result = str('Success sending: ' + str(dataToWrite) + ' to: ' + str(ftpServerName['host']))
			result = {'userId': configUser, 'currentServer': ftpServerName['host'], 'shard': dataToWrite}
		except Exception as e:
			result = ('\nFile Transfer error: ' + str(e))
		
		conn.close()

	except Exception as e:
		result = str('Failed connecting to: ' + str(ftpServerName) + 'error below\n' + str(e))
	try:	conn.close()
	except:	pass


	return result




# from createNetMap.py
def createMap(currentUserId):

	shardList = []
	for i in range(8):
		currentKeyAddr = 'pr/' + str(currentUserId) + '/' + str(i) + '.json.encrypted'
		shardList.append(currentKeyAddr)

	if len(shardList) == 8:
		cluster0 = {'cluster': 0, 'server': 'shardHive1',
					'ogAddrMap': {0: shardList[0],
				  			  	  2: shardList[2]},
					'distributed': False}

		cluster1 = {'cluster': 1, 'server': 'shardHive1',
					'ogAddrMap': {3: shardList[3],
				  			  	  6: shardList[6]},
					'distributed': False}

		cluster2 = {'cluster': 2, 'server': 'shardHive1',
					'ogAddrMap': {5: shardList[5],
				  			  	  1: shardList[1]},
					'distributed': False}

		cluster3 = {'cluster': 3, 'server': 'shardHive1',
					'ogAddrMap': {4: shardList[4],
				  			  	  7: shardList[7]},
					'distributed': False}

		clusterList = [cluster0, cluster1, cluster2, cluster3]

	mapDict = {'userId': currentUserId, 'clusterList': clusterList}
	return mapDict



def processCluster(clusterDict):

	proCluResults, newAddrMap = [], {}
	currentServerName = clusterDict['server']
	currentServer = secrets.servers[currentServerName]	

	serverUser = currentServer['user']

	serverUser = currentServer['user']
	clusterShardList = list(clusterDict['ogAddrMap'].values())
	for shard in clusterShardList:
		shardIndex = clusterShardList.index(shard)
		sftpTransfer = writeFile(currentServer, theUserId, shard)
		#print(sftpTransfer)
		proCluResults.append(sftpTransfer)
		clusterDict.update({'distributed': True})

		rmCommand = 'rm ' + str(shard)
		os.system(rmCommand)
		#print('\nCommented out the RM command')
		#newAddrMap.update({shardIndex: currentServerName})

	return clusterDict









# sftpRead

def transferFile(ftpServerName, userId):
	cnopts, port = pysftp.CnOpts(), 22
	cnopts.hostkeys = None 

	try:	os.mkdir('pr/' + str(userId) + '/tmp/')
	except:	pass
	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		conn.cwd('FTP/hive/')

		#print(conn.listdir())
		#print(conn.pwd)

		try:
			userIdTmpDir = str('pr/'+ str(userId)+'/tmp')
			theFile = conn.get_d(str(userId), userIdTmpDir, preserve_mtime=False)
			responseMsg = {'status': 'success', 'error': None}

		except Exception as e:
			print(e)

			responseMsg = {'status': 'failed', 'error': e}

	except Exception as e:
		print('failed to establish connection to targeted server')
		print('error msg: ' + str(e))

		responseMsg = {'status': 'failed', 'error': e}

	return responseMsg





# processShards.py

def decryptShard(encryptedFileAddr, encryptionKeyAddr):
	with open(encryptedFileAddr, 'rb') as f:
		encryptedFile = f.read()


	try:
		keyFile = open(encryptionKeyAddr)
		encryptionKey = keyFile.read()
		keyFile.close()
		#print('\nSuccess opening shardHive pkey')

	except Exception as e:
		print('\nFailed to open keyfile. error msg below')
		print(e)
		print('\n')

	try:
		fernet = Fernet(encryptionKey)
		decryptedFile = fernet.decrypt(encryptedFile)

	except Exception as e:
		print(e)
		decryptedFile = fernet.decrypt(encryptedFile)
		print(decryptedFile)

		print('\nFailed to decrypt shard. error msg below')
		print(e)
		print('\n')
		#decryptedFile = 'error: ' + str(e)

	return decryptedFile



def decryptAndDelete(inputNetMap2):
	inputConfig = readJson(inputNetMap2)

	currentUserId = inputConfig['userId']
	clusterList = inputConfig['clusterList']
	currentKeyAddr = 'pr/' + str(currentUserId) + '.key'

	dShardDict, ddOutput = {}, ''
	for cluster in clusterList:
		clusterDist = cluster['distributed']
		if clusterDist == True:
			currentOgAddrMap = cluster['ogAddrMap']
			addrList = list(currentOgAddrMap.values())
			for addr in addrList:
				userPubDir = 'pr/' + str(theUserId)
				addrIndex0 = addr.split(userPubDir)[1]
				addrIndex = addrIndex0.split('.json')[0]
				tmpAddr0 = str(addr.replace('/', '/tmp/'))
				tmpAddr = tmpAddr0.replace('pr/tmp', 'pr')
				currentShard = decryptShard(tmpAddr, currentKeyAddr)
				encoding = 'utf-8'
				decShard0 = currentShard.decode(encoding)
				decShard1 = decShard0.replace('"', '')
				decShard2 = decShard1.replace('"', '')

				if decShard2 not in dShardDict:
					dShardDict.update({addrIndex : decShard2})

			#print(dShardDict)
		else:

			currentOgAddrMap = cluster['ogAddrMap']
			addrList = list(currentOgAddrMap.values())
			for addr in addrList:
				#print(addr)
				addrIndex = addr.split('/')[1][0]
				currentShard = decryptShard(addr, currentKeyAddr)
				try:
					encoding = 'utf-8'
					decShard0 = currentShard.decode(encoding)
				except:
					decShard0 = currentShard

				decShard1 = decShard0.replace('"', '')
				decShard2 = decShard1.replace('"', '')
				if decShard2 not in dShardDict:
					dShardDict.update({addrIndex : decShard2})


	sortedDd = list((sorted(dShardDict.items(), key=lambda x:x[0], reverse=False)))
	#print(sortedDd)
	ddOutput = ''
	for dItems in sortedDd:
		sortedValue = dItems[1]
		ddOutput = ddOutput + str(sortedValue)
	

	if logDecryptedShard == True:
		print(ddOutput)
	
	
	return ddOutput

