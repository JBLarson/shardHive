
import paramiko
import pysftp
from ftpCredz import *
from shardFuncs import *


theConfig = 'configs/test3.json'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  



def writeFile(ftpServerName, inputConfig, dataToWrite):


	theConfig = readJsonFunc(inputConfig)
	configUser = theConfig['userId']
	configFileName = theConfig['fileName']

	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		print("connection established successfully")
	except:	print('failed to establish connection to targeted server')




	try:
		conn.cwd('FTP/shardHive/' + str(configUser) + '/' + str(configFileName))
	except:
		conn.mkdir('FTP/shardHive/' + str(configUser) + '/' + str(configFileName))
		conn.cwd('FTP/shardHive/' + str(configUser) + '/' + str(configFileName))


	try:
		conn.put(dataToWrite)
		print('Success transferring: ' + str(dataToWrite))
	except Exception as e:
		print('\nFile Transfer error: ' + str(e))


	conn.close()




write0 = writeFile(pi0, theConfig, '12/test3/0.json.encrypted')
#write1 = writeFile(pi1, theConfig, 'data/1.json.encrypted')
#write2 = writeFile(pi1, theConfig, 'data/2.json.encrypted')
#write3 = writeFile(pi1, theConfig, 'data/3.json.encrypted')





print()

