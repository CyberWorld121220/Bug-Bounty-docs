#!/bin/bash
cd "TestingData/$1/$1_domain"
mkdir "images"
## first 200 sites
isthere=$(ls | grep "list200-${2}.txt")
if [ ${#isthere} -gt 1 ];then
echo "is there"
mkdir "images/200"
while IFS= read -r line; do
/usr/bin/google-chrome --headless --screenshot="images/200/$line.png" "https://$line" --no-sandbox
done < "list200-${2}.txt"
chmod a+rwx "images"
chmod a+rwx images/200
chmod a+rwx images/200/*
else
echo "is not there"
fi
pwd
## first 403 sites
isthere=$(ls | grep "list403-${2}.txt")
if [ ${#isthere} -gt 1 ];then
echo "is there"
mkdir "images/403"
while IFS= read -r line; do
/usr/bin/google-chrome --headless --screenshot="images/403/$line.png" "https://$line" --no-sandbox
done < "list403-${2}.txt"
chmod a+rwx images/403
chmod a+rwx images/403/*
else
echo "is not there"
fi
pwd
## first 404 sites
isthere=$(ls | grep "list404-${2}.txt")
if [ ${#isthere} -gt 1 ];then
echo "is there"
mkdir "images/404"
while IFS= read -r line; do
/usr/bin/google-chrome --headless --screenshot="images/404/$line.png" "https://$line" --no-sandbox
done < "list404-${2}.txt"
chmod a+rwx images/404
chmod a+rwx images/404/*
else
echo "is not there"
fi
pwd
cd ../../../
pwd
