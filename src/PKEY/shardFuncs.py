

import cryptography
from cryptography.fernet import Fernet
import json
import datetime
from time import strftime, strptime
import time
from secrets import *
import secrets
import paramiko
import pysftp
import os



theUserId = 12


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  



#don't delete anything without testing. something else might be relying on dtRn


# create time variables
timeRn = datetime.datetime.now()
dtRn1 = str(strftime("%x") + "_" + strftime("%X"))
dtRn0 = dtRn1.replace('/', '_')
dtRn = dtRn0.replace(':', '_')

# export data to json
def writeJson(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("Success Creating JSON at: " + str(jsonOutAddr))

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput

# import data from json
def readJson(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict






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




def keyGen(keyName):
	key = Fernet.generate_key()
	keyAddr = 'pubRec/' + str(keyName) + '.key'
	file = open(keyAddr, 'wb')
	file.write(key)
	file.close()
	msg = '\nCreated key at: ' + str(keyAddr)
	print(msg)
	return keyAddr





# funcs originally on sftpWrite.py

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

