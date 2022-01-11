#!/Users/jb/Desktop/shardHive/hiveEnv/bin/python3

from shardFuncs import *


def decryptShard(encryptedFileAddr, encryptionKeyAddr):
	with open(encryptedFileAddr, 'rb') as f:
		encryptedFile = f.read()
	keyFile = open(encryptionKeyAddr)
	encryptionKey = keyFile.read()
	keyFile.close()

	fernet = Fernet(encryptionKey)
	decryptedFile = fernet.decrypt(encryptedFile)
	encoding = 'utf-8'
	decryptedFile = decryptedFile.decode(encoding)
	return decryptedFile


def decryptFile(shardConfig):
	decryptedShards = []
	configKey = shardConfig['key']
	shardMap = shardConfig['map']
	mapKeys = list(shardMap.keys())
	for key in mapKeys:
		currentShardAddress = shardMap[key]

		decryptedShard = decryptShard(currentShardAddress, configKey)
		decryptedShards.append(decryptedShard)
	decryptedString = ''
	for shard in decryptedShards:
		decryptedString = str(decryptedString) + str(shard) + ' '
	decryptedString = decryptedString.replace('" "', '')

	return decryptedString

testConfig = readJsonFunc('_id__12_dt__01_09_22_11_35_06.config')
decryptTest = decryptFile(testConfig)
print(decryptTest)
