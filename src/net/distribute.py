#!/usr/bin/python3

from secrets import *
from shardFuncs import *


try:
	jsonOutAddr = '/' + str(ioFile)
	print('\nUser: ' + str(theUserId) + ' Reading Original File From: ' + str(jsonOutAddr))
except:
    pass


print("\n-------------------------------------")
print("Writing to the shardHive Network")
print("-------------------------------------\n")


print("--------------------------------------------------")
justTime, justDate = strftime("%X"), strftime("%x")
print("Started Sharding Algorithm on: " + str(justDate) + " at: " + str(justTime) + "\n")

shardPk = shardAndEncrypt(theUserId, theUserPk)

try:
	outputAddr = 'pr/' + str(theUserId) + '/shardMap.json'
	writeJson(outputAddr, shardPk)
	#print('\nSuccess writing map to: ' + str(outputAddr))
except Exception as e:
    print(e)
	#print('\nFailed to write map: ' + str(e))



justTime, justDate = strftime("%X"), strftime("%x")
print("\nFinished Sharding Algorithm on: " + str(justDate) + " at: " + str(justTime))

print("---------------------------------------------------")

justTime, justDate = strftime("%X"), strftime("%x")
print("Started Distributing Shards on: " + str(justDate) + " at: " + str(justTime) + "\n")



try:
	theMap = createMap(theUserId)
except Exception as e:
	print('\nFailed creating map. Exception below\n\n')
	print(e)


clusterList = theMap['clusterList']
updatedClusterList, currentUser = [], theUserId
for cluster in clusterList:
	if cluster['server'] == 'shardHive1': # need to improve this component in the system
		distributedCluster = processCluster(cluster)
		if distributedCluster not in updatedClusterList:
			updatedClusterList.append(distributedCluster)

	else:
		updatedClusterList.append(cluster)


updatedNetMapConfig = {'userId': theUserId, 'clusterList': updatedClusterList}
#print(updatedNetMapConfig)


try:
	jsonOutAddr = 'pr/' + str(theUserId) + '/netMap.json'
	writeNewNetMap = writeJson(jsonOutAddr, updatedNetMapConfig)
	#print(writeNewNetMap)
except Exception as e:
	print(e)



justTime, justDate = strftime("%X"), strftime("%x")
print("Finished Distributing Shards on: " + str(justDate) + " at: " + str(justTime))

print("---------------------------------------------------\n")

