#!/bin/bash
# starting subfinder tool
echo "Usage => subfind.sh target outputfile"
subfinder -d $1 -v -o subdomains.txt
# starting assetfinder tool
assetfinder --sub-only $1 | tee -a subdomains.txt
# starting amass tool
amass enum -passive -d $1 -o $1_amass.txt
cat $1_amass.txt | tee -a subdomains.txt
rm -rf $1_amass.txt
# moving for Sublist3r
cd Tools
python3 sublist3r.py -d $1 -o ./../$1_sublist3r.txt
cd ..
cat $1_sublist3r.txt | tee -a subdomains.txt
rm -rf $1_sublist3r.txt
sort -u subdomains.txt -o $1_subdomains.txt
rm -rf subdomains.txt
