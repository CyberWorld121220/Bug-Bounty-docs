#!/bin/bash
service crond stop
python3 refresh-pending.py
rm -rf pending.txt
touch pending.txt
rm -rf TestingData/topush.txt
touch TestingData/topush.txt
echo "NotWorking" > presently.txt
service crond start

