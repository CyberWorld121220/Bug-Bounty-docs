#!/bin/bash
while read line; do 
var="$line"
res="${var//[^.]}"
#echo "$res"
echo "${#res}";
if [ ${#res} -eq 2 ]; then
echo "$line" >> "$1_sub_3.txt"
elif [ ${#res} -eq 3 ]; then
echo "$line" >> "$1_sub_4.txt"
else
echo "$line" >> "$1_sub_more.txt"
fi
done < "$1_subdomains.txt"

