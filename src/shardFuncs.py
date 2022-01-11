

import cryptography
from cryptography.fernet import Fernet
import json
import datetime
from time import strftime, strptime
import time



# create time variables
timeRn = datetime.datetime.now()
dtRn = str(strftime("%x") + "_" + strftime("%X"))
dtRn = dtRn.replace('/', '_')
dtRn = dtRn.replace(':', '_')

# export data to json
def createJsonFunc(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("Success Creating JSON at: " + str(jsonOutAddr))

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput

# import data from json
def readJsonFunc(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict






def shardString(inputStr, numShards):

	strLen = len(inputStr)
	shardLen = strLen / numShards
	rangeList0 = []
	for shard in range((numShards+1)):
		shardRange = shard*shardLen
		rangeList0.append(shardRange)

	rangeList1 = []
	for sRange in rangeList0:
		sIndex = rangeList0.index(sRange)
		currentShardRange = rangeList0[sIndex]
		if sIndex > 0:
			lastShardRange = rangeList0[sIndex-1]

			rangePair = [int(lastShardRange), int(currentShardRange)]
			rangeList1.append(rangePair)

	shardList = []	
	for currentRange in rangeList1:
		currentShard = inputStr[currentRange[0]: currentRange[1]]
		shardList.append(currentShard)
	return shardList





def keyGen(keyName):
	key = Fernet.generate_key()
	keyAddr = str(keyName) + '.key'
	file = open(keyAddr, 'wb')
	file.write(key)
	file.close()
	msg = '\nCreated key at: ' + str(keyAddr)
	print(msg)
	return keyAddr




