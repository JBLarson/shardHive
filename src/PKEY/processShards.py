#!/usr/bin/python3


import os
from shardFuncs import *
import secrets



def decryptShard(encryptedFileAddr, encryptionKeyAddr):
	with open(encryptedFileAddr, 'rb') as f:
		encryptedFile = f.read()
	keyFile = open(encryptionKeyAddr)
	encryptionKey = keyFile.read()
	keyFile.close()

	fernet = Fernet(encryptionKey)
	decryptedFile = fernet.decrypt(encryptedFile)
	return decryptedFile





def decryptAndDelete(inputNetMap2):
	inputConfig = readJson(inputNetMap2)


	currentUserId = inputConfig['userId']
	clusterList = inputConfig['clusterList']
	currentKeyAddr = str(currentUserId) + '.key'
	dShardDict, ddOutput = {}, ''
	for cluster in clusterList:
		clusterDist = cluster['distributed']
		if clusterDist == True:
			currentOgAddrMap = cluster['ogAddrMap']
			addrList = list(currentOgAddrMap.values())
			for addr in addrList:
				#print(addr)
				addrIndex = addr.split('/')[1][0]
				tmpAddr = str(addr.replace('/', '/tmp/'))
				#with open(tmpAddr, 'rb') as f:
		
				#	encryptedFile = f.read()

				currentShard = decryptShard(tmpAddr, currentKeyAddr)
				#print(currentShard)

				encoding = 'utf-8'
				decShard0 = currentShard.decode(encoding)
				decShard1 = decShard0.replace('"', '')
				decShard2 = decShard1.replace('"', '')

				if decShard2 not in dShardDict:
					dShardDict.update({addrIndex : decShard2})

		else:

			currentOgAddrMap = cluster['ogAddrMap']
			addrList = list(currentOgAddrMap.values())
			for addr in addrList:
				#print(addr)
				addrIndex = addr.split('/')[1][0]
				currentShard = decryptShard(addr, currentKeyAddr)
				encoding = 'utf-8'
				decShard0 = currentShard.decode(encoding)
				decShard1 = decShard0.replace('"', '')
				decShard2 = decShard1.replace('"', '')
				if decShard2 not in dShardDict:
					dShardDict.update({addrIndex : decShard2})


	sortedDd = list((sorted(dShardDict.items(), key=lambda x:x[0], reverse=False)))
	ddOutput = ''
	for dItems in sortedDd:
		sortedValue = dItems[1]
		ddOutput = ddOutput + str(sortedValue)


	return ddOutput







userNMap2 = str(theUserId) + '/netMap.json'
dd = decryptAndDelete(userNMap2)
print(dd)
'''

sortedDd = list((sorted(dd.items(), key=lambda x:x[0], reverse=False)))
ddOutput = ''

for dItems in sortedDd:
	sortedValue = dItems[1]
	ddOutput = ddOutput + str(sortedValue)
'''


try:
	jsonOutAddr = str(theUserId) + '/pKey.json'
	ddOutputSaved = writeJson(jsonOutAddr, dd)
	print(ddOutputSaved)
except Exception as e:
	print('\nError saving pKey')
	print(e)
