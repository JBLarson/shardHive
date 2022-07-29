#!/usr/bin/python3

import paramiko
import pysftp
import os
from shardFuncs import *
import secrets


print("\n-------------------------------------")
print("Reading from the shardHive Network")
print("-------------------------------------\n")


print("---------------------------------------------------")

justTime, justDate = strftime("%X"), strftime("%x")
print("Started Shard Retrieval on: " + str(justDate) + " at: " + str(justTime))

netMapAddr = 'pr/' + str(theUserId) + '/netMap.json'

theConfig = readJson(netMapAddr)

clusterList = theConfig['clusterList']

for cluster in clusterList:
	distStatus = cluster['distributed']
	if distStatus == True:

		serverName = cluster['server']
		currentServer = secrets.servers[serverName]

		transferFiles = transferFile(currentServer, theUserId)



justTime, justDate = strftime("%X"), strftime("%x")
print("\nFinished Shard Retrieval on: " + str(justDate) + " at: " + str(justTime))

print("---------------------------------------------------")

justTime, justDate = strftime("%X"), strftime("%x")
print("Started Processing Shards on: " + str(justDate) + " at: " + str(justTime))



userNMap2 = 'pr/' + str(theUserId) + '/netMap.json'
dd = decryptAndDelete(userNMap2)


try:
	jsonOutAddr = 'pr/' + str(theUserId) + '/sh_' + str(ioFile)
	ddOutputSaved = writeJson(jsonOutAddr, dd)

except Exception as e:
	print('\nError saving pKey\n')
	print(e)


try:
	jsonOutAddr = 'pr/' + str(theUserId) + '/sh_' + str(ioFile)
	chmodCommand = 'chmod 600 ' + str(jsonOutAddr)
	os.system(chmodCommand)
	#print('Saved Original Files to: ' + str(jsonOutAddr))
except Exception as e:
	print('\nError Saving Original File')
	print(e)


justTime, justDate = strftime("%X"), strftime("%x")
print("\nFinished Processing Shards on: " + str(justDate) + " at: " + str(justTime))
print("---------------------------------------------------")

try:
	jsonOutAddr = 'pr/' + str(theUserId) + '/sh_' + str(ioFile)
	print('\nSaved Original File to: ' + str(jsonOutAddr) + "\n")
except:
    pass
