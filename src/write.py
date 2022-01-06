#!/Users/jb/Desktop/web3/altCoin/jb3nv/bin/python3

from shardFuncs import *

theString = 'Data that will be sharded and encrypted'

shards = shardString(theString, 4)



def encryptShards(shardList):
	
	for shard in shardList:
		shardIndex = str(shardList.index(shard))
		currentKey = keyGen(shardIndex)
		print(currentKey)
		jsonAddr = str(shardIndex) + '.json'
		createCurrentJson = createJsonFunc(jsonAddr, shard)
		print(createCurrentJson)

	for shard in shardList:
		shardIndex = str(shardList.index(shard))

		currentKeyAddr = str(shardIndex) + '.key'
		keyFile = open(currentKeyAddr, 'rb')
		currentKey = keyFile.read()
		keyFile.close()


		currentJsonAddr = str(shardIndex) + '.json'
		with open(currentJsonAddr, 'rb') as f:
			currentJson = f.read()

		fernet = Fernet(currentKey)
		encryptedJson = fernet.encrypt(currentJson)

		encryptedJsonAddr = str(currentJsonAddr) + '.encrypted'

		with open(encryptedJsonAddr, 'wb') as f:
			f.write(encryptedJson)


encryptShardTest = encryptShards(shards)
