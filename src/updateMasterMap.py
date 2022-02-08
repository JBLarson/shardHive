  #!/Users/jb/Desktop/shardHive/shardEnv/bin/python3

from shardFuncs import *
import os
from ftpCredz import *

theConfigAddr = '_id__12_dt__02_06_22_18_52_30.config'
config2 = '_id__12_dt__02_06_22_21_40_46.config'

# will be included with sftpWrite.py writeFile() func

try:
	masterMap = readJsonFunc('masterMap.json')
	print(masterMap)


	def addConfigToMaster(inputConfigAddr, ftpServer, existingMasterMap):
		inputConfig = readJsonFunc(inputConfigAddr)

		masterMapFiles = existingMasterMap['files']


		configMap = inputConfig['map']
		configMapValues = list(configMap.values())

		for value in configMapValues:
			masterMapFiles.append(value)


		return existingMasterMap


	#newMaster = addConfigToMaster(theConfigAddr, pi1, masterMap)
	newMaster = addConfigToMaster(config2, pi1, masterMap)

	createJsonFunc('masterMap.json', newMaster)

except Exception as e:
	print('\nError updating masterMap\n')
	print(e)
	pass

	'''

	try:
		if addConfig not in masterMap:	
			masterMap.update(addConfig)

	except:
		createJsonFunc('masterMap.json', addConfig)
	
except:


	def createMasterMap(inputConfigAddr, ftpServer, dataToWrite):
		inputConfig = readJsonFunc(inputConfigAddr)


		configMap = inputConfig['map']
		configMapValues = list(configMap.values())

		#print(inputConfig)
		ftpServerEthAddr = ftpServer['ethAddr']
		ftpServerDict = {'ftpServer': ftpServer['host'], 'user': inputConfig['userId'], 'ethAddr': ftpServerEthAddr, 'files': configMapValues}

		

		return ftpServerDict


	createMaster = createMasterMap(theConfigAddr, pi1, '0.json.encrypted')

	try:
		if createMaster not in masterMap:	
			masterMap.update(createMaster)
		
	except:
		createJsonFunc('masterMap.json', createMaster)
'''
