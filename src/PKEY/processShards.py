#!/usr/bin/python3


import os
from shardFuncs import *
import secrets



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
	currentKeyAddr = 'pubRec/' + str(currentUserId) + '.key'

	dShardDict, ddOutput = {}, ''
	for cluster in clusterList:
		clusterDist = cluster['distributed']
		if clusterDist == True:
			currentOgAddrMap = cluster['ogAddrMap']
			addrList = list(currentOgAddrMap.values())
			for addr in addrList:
				userPubDir = 'pubRec/' + str(theUserId)
				addrIndex0 = addr.split(userPubDir)[1]
				print(addrIndex0)
				addrIndex = addrIndex0.split('.json')[0]
				print(addrIndex)
				print(addrIndex)
				print(addr)
				tmpAddr0 = str(addr.replace('/', '/tmp/'))
				tmpAddr = tmpAddr0.replace('pubRec/tmp', 'pubRec')
				#with open(tmpAddr, 'rb') as f:
				#print(tmpAddr)		
				#	encryptedFile = f.read()


				currentShard = decryptShard(tmpAddr, currentKeyAddr)



				#print(currentShard)

				encoding = 'utf-8'
				decShard0 = currentShard.decode(encoding)
				decShard1 = decShard0.replace('"', '')
				decShard2 = decShard1.replace('"', '')
				print(decShard2)

				if decShard2 not in dShardDict:
					dShardDict.update({addrIndex : decShard2})

					print(dShardDict)

			print(dShardDict)
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
	print(sortedDd)
	ddOutput = ''
	for dItems in sortedDd:
		sortedValue = dItems[1]
		ddOutput = ddOutput + str(sortedValue)

	return ddOutput



userNMap2 = 'pubRec/' + str(theUserId) + '/netMap.json'
dd = decryptAndDelete(userNMap2)


try:
	jsonOutAddr = 'pubRec/' + str(theUserId) + '/pKey.json'
	ddOutputSaved = writeJson(jsonOutAddr, dd)

except Exception as e:
	print('\nError saving pKey')
	print(e)


try:
	jsonOutAddr = 'pubRec/' + str(theUserId) + '/pKey.json'
	chmodCommand = 'chmod 600 ' + str(jsonOutAddr)
	os.system(chmodCommand)
	print('\nSaved private key to: ' + str(jsonOutAddr)+ '\nSuccess restricting pKey permissions')
except Exception as e:
	print('\nError modifying pKey permissions')
	print(e)

