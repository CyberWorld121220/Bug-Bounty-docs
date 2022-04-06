#!/bin/bash
webanalyze -update
cd "TestingData/$1/$1_domain"
mkdir "technologies"
## first 200 sites
isthere=$(ls | grep "list200-${2}.txt")
if [ ${#isthere} -gt 1 ];then
echo "is there"
mkdir "technologies/200"
while IFS= read -r line; do
result=$(wappalyzer "https://$line")
echo $result >> "list200-tech-$2.txt"
echo $result > "technologies/200/$line.txt"
done < "list200-${2}.txt"
chmod a+rwx "technologies"
chmod a+rwx technologies/200
chmod a+rwx technologies/200/*
else
echo "is not there"
fi
pwd
## first 403 sites
isthere=$(ls | grep "list403-${2}.txt")
if [ ${#isthere} -gt 1 ];then
echo "is there"
mkdir "technologies/403"
while IFS= read -r line; do
result=$(wappalyzer "https://$line")
echo $result >> "list403-tech-$2.txt"
echo $result > "technologies/403/$line.txt"
done < "list403-${2}.txt"
chmod a+rwx technologies/403
chmod a+rwx technologies/403/*
else
echo "is not there"
fi
pwd
## first 404 sites
isthere=$(ls | grep "list404-${2}.txt")
if [ ${#isthere} -gt 1 ];then
echo "is there"
mkdir "technologies/404"
while IFS= read -r line; do
result=$(wappalyzer "https://$line")
echo $result >> "list404-tech-$2.txt"
echo $result > "technologies/404/$line.txt"
done < "list404-${2}.txt"
chmod a+rwx technologies/404
chmod a+rwx technologies/404/*
else
echo "is not there"
fi
pwd
cd ../../../
pwd
