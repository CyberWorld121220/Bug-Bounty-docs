#!/bin/bash
cat subdomains.txt | httprobe | tee -a urls.txt
sort -u urls.txt
wc -l urls.txt
urls=( "first" )
i=0
while IFS= read -r line; do
urls[$i]=$line;
i=$((i + 1))
done < urls.txt
rm -rf urls.txt
sorted_urls=($(echo "${urls[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
echo ${#sorted_urls[*]}
echo "element by element"
x=0
domains=( "first" )
for element in ${sorted_urls[*]}
do
echo $element
if [ $(echo $element | awk '{print substr($0,0,5)}') == "http:" ]; then
domains[$x]="$(echo $element | awk '{print substr($0,8)}')"
x=$((x + 1))
elif [ $(echo $element | awk '{print substr($0,0,5)}') == "https" ]; then
domains[$x]="$(echo $element | awk '{print substr($0,9)}')"
x=$((x + 1))
else
echo "not a valid domain"
fi

#IFS='://'
#read -ra ADDR <<< "$element"
#echo ${ADDR[1]}
#IFS=' '
done
sorted_domains=($(echo "${domains[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
for domain in ${sorted_domains[*]}
do
echo "$domain" >> new.txt
done
