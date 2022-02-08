#!/Users/jb/Desktop/shardHive/shardEnv/bin/python3


import paramiko
import pysftp
from ftpCredz import *
from shardFuncs import *



cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  



def checkNode(ftpServerName, shUser, masterMapInput):

	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		#print("connection established successfully")
	except:	print('\nfailed to establish connection to targeted server\n')

	conn.cwd('FTP/shardHive/')

	masterMap = readJsonFunc(masterMapInput)

	masterMapFiles = masterMap['files']

	for fileAddr in masterMapFiles:


		dirExists = conn.exists(fileAddr)


		print(str(fileAddr) + ' exists: ' + str(dirExists))


	conn.close()



checkTest = checkNode(pi1, 12, 'masterMap.json')

