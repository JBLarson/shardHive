#!/usr/bin/env python


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import strftime, strptime
import datetime


# create time variables
timeRn = datetime.datetime.now()
dtRn0 = str(strftime("%x") + " " + strftime("%X"))
print("\nshardHive RFID Write Executed at: " + str(dtRn0))


reader = SimpleMFRC522()


sh3 = '0x3eb393abc3bcf117d1952b454ee293f66e5ca762'



currentAddr = sh3


try:
        id = reader.write('sh3')
        text = reader.write(currentAddr)
        print("\nClient Authorized at: " + str(strftime("%x") + " " + strftime("%X")))
        print("ID Code: " + str(id))
        print("Ethereum Wallet: " + str(text))

        print(text)
finally:
        GPIO.cleanup()







dtRn1 = str(strftime("%x") + " " + strftime("%X"))
print("\nshardHive RFID Write Terminated at: " + str(dtRn1))


