

import ftplib
from ftpCredz import *
from shardFuncs import *
import os


#print(dtRn)

inputConfig = '_id__12_dt__01_11_22_18_33_19.config'
testConfig = readJsonFunc(inputConfig)

# create user and dt variables from config file
configSplit = inputConfig.split('__')
configUser = configSplit[1].replace('_dt', '')
configDT = configSplit[2].replace('.config', '')


theFile = 'theString.txt'



def readFTPcontent(user, ftpServerName):

	data, fileNames = [], []

	ftpServer = ftplib.FTP(ftpServerName['host'])
	ftpServer.login(ftpServerName['user'], ftpServerName['pass'])
	#userDir = '/shardHive/' + str(user) + '/' + str(configDT)
	userDir = '/shardHive/' + str(user) + '/'

	ftpServer.cwd(userDir)


	#ftpPWD = ftpServer.pwd()
	#rint(ftpPWD)

	try:
		#dirNames = ftpServer.mlsd('shardHive0/12')
		dirNames = ftpServer.nlst()
		print('\nshardHive directories: ' + str(dirNames))



		if len(dirNames) > 0:
			for currentDir in dirNames:
				ftpServer.cwd(str(currentDir) + '/')
				filematch = '*.*'
				fileNames = list(ftpServer.nlst(filematch))
				print('\nContents of: ' + str(currentDir))
				print(fileNames)


				ftpServer.cwd('/shardHive/12')
		


		print(ftpServer.nlst())

		try:	ftpServer.quit()
		except: pass



	except Exception as e:
		print(e)

		try:	ftpServer.quit()
		except: pass




writeTest = readFTPcontent('12', pi0)

print()
