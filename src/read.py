#!/Users/jb/Desktop/web3/altCoin/jb3nv/bin/python3

from shardFuncs import *

testShardList = ['0.json.encrypted', '1.json.encrypted', '2.json.encrypted', '3.json.encrypted']


def decryptShard(encryptedFileAddr, encryptionKeyAddr):
	with open(encryptedFileAddr, 'rb') as f:
		encryptedFile = f.read()
	keyFile = open(encryptionKeyAddr)
	encryptionKey = keyFile.read()
	keyFile.close()

	fernet = Fernet(encryptionKey)
	decryptedFile = fernet.decrypt(encryptedFile)
	return decryptedFile



def decryptShards(shardList):
	decryptedShards = []
	for encryptedShard in shardList:
		shardIndex = shardList.index(encryptedShard)
		encryptedShardAddr, encryptionKeyAddr = str(shardIndex) + '.json.encrypted', str(shardIndex) + '.key'
		decryptedShard = decryptShard(encryptedShardAddr, encryptionKeyAddr)
		encoding = 'utf-8'
		decryptedShard = decryptedShard.decode(encoding)
		decryptedShards.append(decryptedShard)
	decryptedString = ''
	for shard in decryptedShards:
		decryptedString = str(decryptedString) + str(shard) + ' '
	decryptedString = decryptedString.replace('" "', '')
	return decryptedString


decryptTest = decryptShards(testShardList)
print(decryptTest)
