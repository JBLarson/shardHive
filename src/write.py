#!/usr/local/bin/python3

from shardFuncs import *
import os


theString = '{"words": "testing words in dictionary / json format", "andNum": 7, "moreWords": "other testing words", "andNum2": 0423}'

shards = shardString(theString, 4)



def encryptShards(shardList, userId, fileName):
	
	shardConfig, shardMap = {}, {}
	

	# create user dir if it doesnt exist
	try:	os.system('mkdir ' + str(userId) + '/')
	except:	pass

	# create user dir if it doesnt exist
	try:	os.system('mkdir ' + str(userId) + '/' + str(fileName))
	except:	pass

	# create user tmp dir
	try:	os.system('mkdir ' + str(userId) + '/' + str(fileName) + '/tmp')
	except:	pass



	# create key or open key

	try:
		currentKeyAddr = (str(userId) + '.key')

		keyFile = open(currentKeyAddr, 'rb')

		currentKey = keyFile.read()
		print('key exists')
	except:
		currentKeyAddr = keyGen(userId)



		keyFile = open(currentKeyAddr, 'rb')
	
		currentKey = keyFile.read()
	
	keyFile.close()


	# write unencrypted json in tmp dir
	for shard in shardList:
		shardIndex = str(shardList.index(shard))
		jsonAddr = str(userId) + '/' + str(fileName) + '/tmp/' + str(shardIndex) + '.json'
		createCurrentJson = createJsonFunc(jsonAddr, shard)

	for shard in shardList:
		shardIndex = str(shardList.index(shard))

		currentJsonAddr = str(userId) + '/' + str(fileName) + '/' + str(shardIndex) + '.json'
		currentTmpJsonAddr = str(userId) + '/' + str(fileName) + '/tmp/' + str(shardIndex) + '.json'

		with open(currentTmpJsonAddr, 'rb') as f:
			currentJson = f.read()

		fernet = Fernet(currentKey)
		encryptedJson = fernet.encrypt(currentJson)

		encryptedJsonAddr = str(currentJsonAddr) + '.encrypted'

		with open(encryptedJsonAddr, 'wb') as f:
			f.write(encryptedJson)

		shardMap.update({shardIndex: encryptedJsonAddr})

	os.system('rm -r ' + str(userId) + '/' + str(fileName) + '/tmp')



	shardConfig.update({'key': currentKeyAddr, 'fileName': fileName, 'dt': dtRn, 'userId': userId, 'map': shardMap})





	configPath = 'configs/' + str(fileName) + '.json'

	createJsonFunc(configPath, shardConfig)

	return shardConfig




encryptShardTest = encryptShards(shards, 12, 'test3')

print(encryptShardTest)

