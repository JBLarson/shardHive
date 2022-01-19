

import ftplib
from ftpCredz import *
from shardFuncs import *


def serverMsg(ftpServerName):
	try:
		ftpServer = ftplib.FTP(ftpServerName['host'])
		ftpServer.login(ftpServerName['user'], ftpServerName['pass'])
		ftpStatus = ftpServer.getwelcome()
		ftpServer.quit()

		if ftpStatus == '220 (vsFTPd 3.0.3)':
			ftpMsg = ('server: ' + str(ftpServerName['host']) + ' is online')


	except Exception as e:
		ftpMsg = str(ftpServerName['host']) + ' ' + str(e)

		try:	ftpServer.quit()
		except: pass
	return ftpMsg

pi0Test, pi1Test, pi2Test = serverMsg(pi0), serverMsg(pi1), serverMsg(pi2)



print(pi0Test)
print(pi1Test)
print(pi2Test)


