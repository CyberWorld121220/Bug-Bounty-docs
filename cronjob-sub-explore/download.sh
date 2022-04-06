#!/bin/bash
read -r target<pull.txt
if [ ${#target} -gt 1 ];
then
echo "Locking ${target} for download ---===>>>"
python3 download.py -d $target
echo "Rest!"
fi
