

import cryptography
from cryptography.fernet import Fernet
import json
import datetime
from time import strftime, strptime
import time
from secrets import *
from shardFuncs import *
import os
import sys



def shardAndEncrypt(userId, pKey):

	# create user dir if it doesnt exist
	try:	os.system('mkdir ' + 'pubRec/' + str(userId) + '/')
	except Exception: pass

	# create user tmp dir
	try:	os.system('mkdir ' + 'pubRec/' + str(userId) + '/tmp')
	except Exception:	pass



	# need to test if userKey already exists so it isn't overwritten
	try:
		currentKeyAddr = (str(userId) + '.key')
		keyFile = open(currentKeyAddr, 'rb')
		currentKey = keyFile.read()
		print('Success opening: ' + str(currentKeyAddr))
	except:

		currentKeyAddr = keyGen(userId)
		print('\nFailed to open existing shardKey. Creating a new one')
		keyFile = open(currentKeyAddr, 'rb')
		currentKey = keyFile.read()
	
	keyFile.close()
	# end of key opening / creation


	pkShards = shardString(pKey, 8)
	#print(pkShards)


	# write unencrypted json in tmp dir

	shardDict = {}
	for shard in pkShards:
		shardIndex = str(pkShards.index(shard))
		jsonAddr = 'pubRec/' + str(userId) + '/tmp/' + str(shardIndex) + '.json'
		createCurrentJson = writeJson(jsonAddr, shard)

	# encrypt unencrypted shards
	for shard in pkShards:
		shardIndex = str(pkShards.index(shard))

		currentJsonAddr = 'pubRec/' + str(userId) + '/' + str(shardIndex) + '.json'
		currentTmpJsonAddr = 'pubRec/' + str(userId) + '/tmp/' + str(shardIndex) + '.json'

		with open(currentTmpJsonAddr, 'rb') as f:
			currentJson = f.read()

		fernet = Fernet(currentKey)
		encryptedJson = fernet.encrypt(currentJson)

		encryptedJsonAddr = str(currentJsonAddr) + '.encrypted'

		with open(encryptedJsonAddr, 'wb') as f:
			f.write(encryptedJson)

		shardDict.update({shardIndex: encryptedJsonAddr})

	# remove tmp dir
	try:	os.system('rm -rf ' + 'pubRec/' + str(userId) + '/tmp')
	except Exception:	pass


	return shardDict






theUserPk = pKeys['jTest']


time = datetime.datetime.now()
dtRn = str(strftime("%x") + " " + strftime("%X"))
justTime, justDate = strftime("%X"), strftime("%x")
print("\nExecuted Initial Sharding Script on: " + str(justDate) + " at: " + str(justTime) + "\n")


shardPk = shardAndEncrypt(theUserId, theUserPk)

#print('\nshardAndEncrypt function output: ' + str(shardPk))


try:
	outputAddr = 'pubRec/' + str(theUserId) + '/shardMap.json'
	writeJson(outputAddr, shardPk)
	print('\nSuccess writing map to: ' + str(outputAddr))
except Exception as e:
	print('\nFailed to write map: ' + str(e))
