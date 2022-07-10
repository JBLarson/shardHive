#!/usr/bin/python3


from shardFuncs import *
import secrets
import sys

try:
	pKeyAddr = sys.argv[1]

	inputKey = readJson(pKeyAddr)

	allTestkeys = list(secrets.pKeys.values())

	for testKey in allTestkeys:
		if str(inputKey).strip() == str(testKey).strip():
			print()
			print(str(testKey[-4:]) + ' matches: ' + str(inputKey[-4:]))
			print()

		else:
			try:
				print(str(testKey[-4:]) + ' not a match with: ' + str(inputKey[-4:]))
			except:
				pass


except Exception as e:
	print(e)