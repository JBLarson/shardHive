

from ethFuncs import *
from web3 import Web3
import json
from infuraUrl import infuraUrl
from secrets import pKeys
from time import strftime




print('\n')



web3 = Web3(Web3.HTTPProvider(infuraUrl))

account1 = '0x2C2E5b824EA2BcE625943aF15e1bBD86630B37EF'
account1pk = pKeys['jTest']

account2 = '0x983C36a518c56b0FCE99AA8a4aed40913DC469CE'
account2pk = pKeys['dolores']

account3 = '0xc838C62098f8C4597908BE707130F63eCeC2ffB7'
account3pk = pKeys['shardHive']


jb3TokenAddress = '0xa51b997E0203136b4fA8c1017829aB8E77eE0b6E'




justTime, justDate = strftime("%X"), strftime("%x")
print("\nExecuted Query on: " + str(justDate) + " at: " + str(justTime) + "\n\n")






#sendJB3Tokens = sendAltCoin(account1, account1pk, account3, jb3TokenAddress, 110000)
sendJB3Tokens = sendAltCoin(account2, account2pk, account3, jb3TokenAddress, 118800)




justTime, justDate = strftime("%X"), strftime("%x")
print("\nCompleted Query on: " + str(justDate) + " at: " + str(justTime) + "\n\n")
