
import paramiko
import pysftp
from ftpCredz import *
from shardFuncs import *
import os


theConfig = 'configs/test3.json'



def transferFile(ftpServerName, inputConfigAddr):


	theConfig = readJsonFunc(inputConfigAddr)

	configUser = theConfig['userId']
	configFileName = theConfig['fileName']


	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		print("connection established successfully")
	except Exception as e:
		print('failed to establish connection to targeted server')
		print('error msg: ' + str(e))

	conn.cwd('FTP/shardHive/' + str(configUser) + '/')
	print(conn.listdir())
	"""
	try:
		os.mkdir(str(configUser) + '/' + str(configDT))
	except Exception as e:
		print('\nUser / Date Dir exists')
		print(e)
		print('\n')

	theFile = conn.get_d(str(configDT), str(configUser) + '/' + str(configDT))
	"""


def decryptAndDelete(inputConfigAddr):
	inputConfig = readJsonFunc(inputConfigAddr)


	configMap = inputConfig['map']
	configKey = inputConfig['key']

	print(configKey)

	# create user and dt variables from config file
	configSplit = inputConfigAddr.split('__')
	configUser = configSplit[1].replace('_dt', '')
	configDT = configSplit[2].replace('.config', '')


	configMapValues = list(configMap.values())

	shards = []

	#print('\n' + str(configMapValues) + '\n')

	for value in configMapValues:
		print('File to decrypt: ' + str(value))
		
		with open("12.key", "rb") as k:
			keyFile = k.read()

		k.close()

		fern = Fernet(keyFile)


		with open(value, 'rb') as f:
			encFile = f.read()

		f.close()

		print(encFile)


		decFile = fern.decrypt(encFile)

		print(decFile)

		#decryptedShard = decryptShard(value, configKey)
		shards.append(decryptedShard)


	ogFile = ''
	for shard in shards:
		ogFile = ogFile + shard
	
	print('removing ' + str(str(configUser) + '/' + str(configDT)))
	#os.system('rm -r ' + str(configUser) + '/' + str(configDT))


	return ogFile

	# need to use os library to delete encrypted files after decryption


transferTest = transferFile(pi0, theConfig)

#decryptedFile = decryptAndDelete(theConfig)
#print(decryptedFile)

