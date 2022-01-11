#!/Users/jb/Desktop/shardHive/hiveEnv/bin/python3

from shardFuncs import *
import sys
import cryptography
from cryptography.fernet import Fernet
import os

#fileInput = sys.argv[1]
#fileInput = 'theString.txt'
fileInput = 'testJson.json'


fileType = fileInput.split('.')[1].lower()


if fileType == 'txt':
	fileContent = ''
	with open(fileInput, 'r') as f:
		for line in f:
			fileContent = fileContent + line

elif fileType == 'json':
	fileContent = readJsonFunc(str(fileInput))


shards = shardString(str(fileContent), 8)



def createConfig(shardList, userId):

	shardConfig, shardMap = {}, {}
	# concat userId and dtRn to create key
	idAndDt = 'id__' + str(userId) + '_dt__' + str(dtRn)
	currentKeyAddr = keyGen(idAndDt)
	keyFile = open(currentKeyAddr, 'rb')
	currentKey = keyFile.read()
	keyFile.close()

	for shard in shardList:
		shardIndex = shardList.index(shard)

		jsonAddr = 'data/' + str(shardIndex) + '.json'
		createCurrentJson = createJsonFunc(jsonAddr, shard)

		with open(jsonAddr, 'rb') as f:
			currentJson = f.read()

		fernet = Fernet(currentKey)
		encryptedJson = fernet.encrypt(currentJson)

		encryptedJsonAddr = str(jsonAddr) + '.encrypted'

		with open(encryptedJsonAddr, 'wb') as f:
			f.write(encryptedJson)

		# remove unencrypted json
		os.remove(jsonAddr)


		shardMap.update({shardIndex: encryptedJsonAddr})




	shardConfig.update({'key': currentKeyAddr, 'dt': dtRn, 'userId': userId, 'map': shardMap})

	configAddr = '_id__' + str(userId) + '_dt__' + str(dtRn) + '.config'
	saveConfig = createJsonFunc(configAddr, shardConfig)

	return shardConfig

configTest = createConfig(shards, '12')
#configAddr = '_id__' + str(configTest['userId']) + '_dt__' + str(configTest['dt']) + '.json'


print('\n')
print(configTest)


