
import paramiko
import pysftp
from ftpCredz import *
from shardFuncs import *
import os

#theConfig = '_id__12_dt__02_06_22_18_52_30.config'
theConfig = '_id__12_dt__02_06_22_21_40_46.config'



def transferFile(ftpServerName, inputConfig):


	testConfig = readJsonFunc(inputConfig)

	# create user and dt variables from config file
	configSplit = inputConfig.split('__')
	configUser = configSplit[1].replace('_dt', '')
	configDT = configSplit[2].replace('.config', '')

	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		print("connection established successfully")
	except:	print('failed to establish connection to targeted server')

	conn.cwd('FTP/shardHive/' + str(configUser) + '/')
	print(conn.listdir())

	try:
		os.mkdir(str(configDT))
	except Exception as e:
		print(e)

	theFile = conn.get_d(str(configDT), str(configDT))


def decryptAndDelete(inputConfigAddr):
	inputConfig = readJsonFunc(inputConfigAddr)


	configMap = inputConfig['map']
	configKey = inputConfig['key']

	

	# create user and dt variables from config file
	configSplit = inputConfigAddr.split('__')
	configUser = configSplit[1].replace('_dt', '')
	configDT = configSplit[2].replace('.config', '')


	configMapValues = list(configMap.values())

	shards = []

	for value in configMapValues:
		decryptedShard = decryptShard(value, configKey)
		shards.append(decryptedShard)

	ogFile = ''
	for shard in shards:
		ogFile = ogFile + shard
	print(ogFile)

readTest = transferFile(pi1, theConfig)
decryptDeleteTest = decryptAndDelete(theConfig)


