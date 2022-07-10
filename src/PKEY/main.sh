#!/bin/bash

python3 shardPk.py && python3 createNetMap.py && python3 sftpRead.py && python3 processShards.py

ls -ltr

