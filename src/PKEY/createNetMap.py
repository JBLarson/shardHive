

from shardFuncs import *


def createMap(currentUserId):

	shardList = []
	for i in range(8):
		currentKeyAddr = str(currentUserId) + '/' + str(i) + '.json.encrypted'
		shardList.append(currentKeyAddr)

	if len(shardList) == 8:
		cluster0 = {'cluster': 0, 'server': 'pi0',
					'ogAddrMap': {0: shardList[0],
				  			  	  2: shardList[2]},
					'distributed': False}

		cluster1 = {'cluster': 1, 'server': 'pi0',
					'ogAddrMap': {3: shardList[3],
				  			  	  6: shardList[6]},
					'distributed': False}

		cluster2 = {'cluster': 2, 'server': 'crowPi',
					'ogAddrMap': {5: shardList[5],
				  			  	  1: shardList[1]},
					'distributed': False}

		cluster3 = {'cluster': 3, 'server': 'crowPi',
					'ogAddrMap': {4: shardList[4],
				  			  	  7: shardList[7]},
					'distributed': False}

		clusterList = [cluster0, cluster1, cluster2, cluster3]

	mapDict = {'userId': currentUserId, 'clusterList': clusterList}
	return mapDict

try:
	theMap = createMap(theUserId)
	#print('\nSuccess creating netMap1\n')
	#print(theMap)
except Exception as e:
	print('\nFailed creating map. Exception below\n\n')
	print(e)


def processCluster(clusterDict):

	proCluResults, newAddrMap = [], {}
	currentServerName = clusterDict['server']
	currentServer = secrets.servers[currentServerName]	

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


clusterList = theMap['clusterList']
updatedClusterList, currentUser = [], theUserId
for cluster in clusterList:
	if cluster['server'] == 'pi0':	
		distributedCluster = processCluster(cluster)
		if distributedCluster not in updatedClusterList:
			updatedClusterList.append(distributedCluster)

	else:
		updatedClusterList.append(cluster)


updatedNetMapConfig = {'userId': theUserId, 'clusterList': updatedClusterList}
print(updatedNetMapConfig)


try:
	jsonOutAddr = str(theUserId) + '/netMap.json'
	writeNewNetMap = writeJson(jsonOutAddr, updatedNetMapConfig)
	print(writeNewNetMap)
except Exception as e:
	print(e)


