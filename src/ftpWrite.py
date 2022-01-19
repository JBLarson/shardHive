

import ftplib
from ftpCredz import *
from shardFuncs import *
from ftplib import FTP


def writeToFtp(ftpServerName, dirToWrite, fileToWrite):
	ftpObject = ftplib.FTP(ftpServerName['host'])
	ftpObject.login(ftpServerName['user'], ftpServerName['pass'])

	
	try:
		ftpChangeDirMsg = ftpObject.cwd(dirToWrite);
	except:
		ftpMkdirMsg = ftpObject.mkd(dirToWrite);
		ftpChangeDirMsg = ftpObject.cwd(dirToWrite);


	fileObject = open(fileToWrite, 'rb')
	fileToBeSavedAs = 'theString.txt'

	ftpCommand = "STOR %s"%fileToBeSavedAs

	ftpWriteResponse = ftpObject.storbinary(ftpCommand, fp=fileObject)
	print(ftpWriteResponse)

	ftpObject.quit()


theString = 'theString.txt'
shardDir = '/shardHive/12/01_18_22_20_49_32'
writeTest = writeToFtp(pi0, shardDir, theString)

