

import ftplib
from ftpCredz import *
from shardFuncs import *
import os

inputConfig = '_id__12_dt__01_11_22_18_33_19.config'
testConfig = readJsonFunc(inputConfig)


print(testConfig)

print('\n')


def getFile(ftpConnection, theFileName):
	try:
		destinationAddr = 'tmp/' + str(theFileName)
		ftpConnection.retrbinary('RETR ' + str(theFileName), open(destinationAddr, 'wb').write)
	except Exception as e:
		print('\nError fetching file: ' + str(e))


def readShards(targetDir, ftpServerName, shardConfig):

	data, fileNames = [], []


	ftpServer = ftplib.FTP(ftpServerName['host'])
	ftpServer.login(ftpServerName['user'], ftpServerName['pass'])

	ftpServer.cwd(targetDir)
	filematch = '*.*'
	fileNames = list(ftpServer.nlst(filematch))


	#print('\nFiles on server: ' + str(ftpServerName['host']))
	#print(fileNames)
	
	for file in fileNames:	writeFileToTmp = getFile(ftpServer, file)

	ftpServer.quit()


	shardKey = shardConfig['key']

	shards = []
	for file in fileNames:
		currentShardAddr = str('tmp/'+str(file))
		
		decryptedShard = decryptShard(currentShardAddr, shardKey)
		shards.append(decryptedShard)

	os.system('rm -r tmp')
	os.mkdir('tmp')
		#print(decryptedShard)
	return shards









def recreateFile2Servers(theConfig, server0, server1):

	# create user and dt variables from config file
	configSplit = inputConfig.split('__')
	configUser = configSplit[1].replace('_dt', '')
	configDT = configSplit[2].replace('.config', '')


	shardDir = '/shardHive/' + str(configUser) + '/' + str(configDT)

	shardList0 = readShards(shardDir, server0, theConfig)
	shardList1 = readShards(shardDir, server1, theConfig)


	shardList = shardList0 + shardList1
	theFile = ''
	for shard in shardList:
		theFile = theFile + shard
	return theFile


recreateFileTest = recreateFile2Servers(testConfig, pi0, pi1)

print('\nOriginal file: ' + str(recreateFileTest))



