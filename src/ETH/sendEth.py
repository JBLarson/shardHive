#!/usr/bin/python3


from ethFuncs import *
from web3 import Web3
from infuraUrl import infuraUrl
from secrets import pKeys
import os
import time


w3 = Web3(Web3.HTTPProvider(infuraUrl))


testingWallet0 = '0xc838C62098f8C4597908BE707130F63eCeC2ffB7' # shardhive test
testingWallet1 = '0x2C2E5b824EA2BcE625943aF15e1bBD86630B37EF' # jTest
testingWallet2 = '0x983C36a518c56b0FCE99AA8a4aed40913DC469CE' # dolores


sendTest = sendEther(testingWallet2, pKeys['dolores'], testingWallet1, 1.6484)

