
import paramiko
import pysftp
import secrets
from shardFuncs import *
import os



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






theConfigAddr = str(theUserId) + '/netMap.json'
theConfig = readJson(theConfigAddr)
#print(theConfig)


updatedClusterList, currentUser, clusterList = [], theConfig['userId'], theConfig['clusterList']

for cluster in clusterList:

	if cluster['server'] == 'pi0':


		distributedCluster = processCluster(cluster)
		updatedClusterList.append(distributedCluster)
	else:
		distributedCluster = processCluster(cluster)
		updatedClusterList.append(distributedCluster)

		#if cluster not in updatedClusterList:
		#	updatedClusterList.append(cluster)

updatedNetMapConfig = {'userId': theUserId, 'clusterList': updatedClusterList}


try:
	jsonOutAddr = str(theUserId) + '/netMap2.json'
	writeNewNetMap = writeJson(jsonOutAddr, updatedNetMapConfig)
	print(writeNewNetMap)
except Exception as e:
	print(e)



