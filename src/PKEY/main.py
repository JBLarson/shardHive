

import os
from shardFuncs import *


try:
	shardPkScript = os.system('python3 shardPk.py')
	createNetMap = os.system('python3 createNetMap.py')
	sftpRead = os.system('python3 sftpRead.py')
	processShards = os.system('python3 processShards.py')

	#time.sleep(5)
	#print('fin')

except Exception as e:
	print(e)

