#!/usr/bin/python3


import sys
import json


# import data from json
def readJsonFunc(jsonInAddr):
	with open(jsonInAddr, 'r') as r:
		jsonOutputDict = json.load(r)
	return jsonOutputDict


inputJsonAddr = sys.argv[1]

inputJson = readJsonFunc(inputJsonAddr)

prettyJson = json.dumps(inputJson, indent=4)

print(prettyJson)
