#!/usr/bin/python3

from shardHiveEVM import *
from secrets import currentShContract
import json
from time import sleep
import sys
from mfrc522 import SimpleMFRC522


rfidReader = SimpleMFRC522()





def writeJson(jsonOutAddr, jsonData):
	try:
		with open(jsonOutAddr, 'w') as fp1: json.dump(jsonData, fp1)
		functionOutput = ("\nSuccess Creating JSON at: " + str(jsonOutAddr) + "\n")

	except Exception as e:
		functionOutput = "\nFailed to create JSON. Error msg:\n" + str(e)

	return functionOutput





print("\n-----------------------------------------------")
print("Launched shardHive v0.0.2 RFID Terminal")
print("-----------------------------------------------\n")

id, content = rfidReader.read()

print('RFID ID: ' + str(id))

print('RFID Content: ' + str(content))

content0 = content.strip()




ethBalance = fetchETHBalance(content0)
print('\nRopsten Test-Net Ether: ' + str(ro4(ethBalance['bal'])))



altBalance = fetchAltBalance(content0, currentShContract)
print('shardHive v0.0.2 Test Tokens: ' + str(altBalance))




addressDict = {"rfidId": str(id), "address": content0}




try:
    print(writeJson('jTest.json', addressDict))

except Exception as e:
    print('\nFailed to save address')
    print(e)
    pass

