
import paramiko
import pysftp
import os

from shardFuncs import *
import secrets



def transferFile(ftpServerName, userId):
	cnopts, port = pysftp.CnOpts(), 22
	cnopts.hostkeys = None 

	try:	os.mkdir('pubRec/' + str(userId) + '/tmp/')
	except:	pass
	try:
		conn = pysftp.Connection(host=ftpServerName['host'],port=port, username=ftpServerName['user'], password=ftpServerName['pass'], cnopts=cnopts)
		conn.cwd('FTP/hive/')

		#print(conn.listdir())
		#print(conn.pwd)

		try:
			userIdTmpDir = str('pubRec/'+ str(userId)+'/tmp')
			theFile = conn.get_d(str(userId), userIdTmpDir, preserve_mtime=False)
			responseMsg = {'status': 'success', 'error': None}

		except Exception as e:
			print(e)

			responseMsg = {'status': 'failed', 'error': e}

	except Exception as e:
		print('failed to establish connection to targeted server')
		print('error msg: ' + str(e))

		responseMsg = {'status': 'failed', 'error': e}

	return responseMsg



netMapAddr = 'pubRec/' + str(theUserId) + '/netMap.json'

theConfig = readJson(netMapAddr)

clusterList = theConfig['clusterList']

for cluster in clusterList:
	distStatus = cluster['distributed']
	if distStatus == True:

		serverName = cluster['server']
		currentServer = secrets.servers[serverName]

		transferFiles = transferFile(currentServer, theUserId)






print('\ncompleted SFTP shard retrieval script\n')

