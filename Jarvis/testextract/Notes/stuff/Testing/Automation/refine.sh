#!/bin/bash
# subdomains refining
while IFS= read -r line; do
x=$IFS
IFS='.'
# Reading the split string into array
read -ra arr <<< "$line"
domain_name=${arr[-2]}
## refining domains and saving to a file
if [ $domain_name == "${2}" ];then
echo "$line" >> "${2}_refined.txt"
fi
done < $1

