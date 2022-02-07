#!/usr/bin/python3


import paramiko
import pysftp
from ftpCredz import *


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  

def readDirs(ftpServerName, shUser):

	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		print("connection established successfully")
	except:	print('\nfailed to establish connection to targeted server\n')

	conn.cwd('FTP/shardHive/' + str(shUser))

	userDirs = conn.listdir()


	for uDir in userDirs:
		print('\nContent of: ' + str(uDir))
		conn.cwd(uDir)
		print(conn.listdir())
		conn.cwd('..')
	conn.close()




#readTest = readDirs(pi0, 12)
readTest = readDirs(pi1, 12)




print()
