
import paramiko
import pysftp
from ftpCredz import *
from shardFuncs import *


theConfig = '_id__12_dt__02_06_22_18_52_30.config'



cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  



def writeFile(ftpServerName, inputConfig, dataToWrite):


	testConfig = readJsonFunc(inputConfig)

	# create user and dt variables from config file
	configSplit = inputConfig.split('__')
	configUser = configSplit[1].replace('_dt', '')
	configDT = configSplit[2].replace('.config', '')

	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		print("connection established successfully")
	except:	print('failed to establish connection to targeted server')

	try:
		conn.cwd('FTP/shardHive/' + str(configUser) + '/' + str(configDT))
	except:
		conn.mkdir('FTP/shardHive/' + str(configUser) + '/' + str(configDT))
		conn.cwd('FTP/shardHive/' + str(configUser) + '/' + str(configDT))

	conn.put(dataToWrite)

	conn.close()




write0 = writeFile(pi1, theConfig, 'data/0.json.encrypted')
write1 = writeFile(pi1, theConfig, 'data/1.json.encrypted')
write2 = writeFile(pi1, theConfig, 'data/2.json.encrypted')
write3 = writeFile(pi1, theConfig, 'data/3.json.encrypted')
write4 = writeFile(pi1, theConfig, 'data/4.json.encrypted')
write5 = writeFile(pi1, theConfig, 'data/5.json.encrypted')
write6 = writeFile(pi1, theConfig, 'data/6.json.encrypted')
write7 = writeFile(pi1, theConfig, 'data/7.json.encrypted')




print()
