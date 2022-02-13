#!/Users/jb/Desktop/shardHive/shardEnv/bin/python3


import paramiko
import pysftp
from ftpCredz import *
from shardFuncs import *



cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  

# first do a check of what nodes are online, put those server names in list
# loop through the 'files' list of each of those nodes to check if they are still hosting



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

