#!/bin/bash
# starting subfinder tool
echo "Usage => ./subfind.sh target output_save_to_file_without_extension"
subfinder -d $1 -v -o subdomains.txt
# starting assetfinder tool
echo "Assetfinder tool started"
assetfinder --sub-only $1 | tee -a subdomains.txt
# starting amass tool
echo "Amass tool started"
amass enum -passive -d $1 -o $1_amass.txt
cat $1_amass.txt | tee -a subdomains.txt
rm -rf $1_amass.txt
# moving for Sublist3r
echo "Sublist3r tool started"
cd Tools
python3 sublist3r.py -d $1 -o ./../$1_sublist3r.txt
cd ..
cat $1_sublist3r.txt | tee -a subdomains.txt
rm -rf $1_sublist3r.txt
sort -u subdomains.txt -o $2_subdomains.txt
rm -rf subdomains.txt
