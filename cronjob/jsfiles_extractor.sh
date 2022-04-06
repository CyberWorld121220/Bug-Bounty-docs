gau -subs $1 | grep '.js$' >> $1_vul1.txt
waybackurls $1 | grep '.js$' >> $1_vul2.txt
subfinder -d $1 | httpx | subjs >> $1_vul3.txt
cat $1_vul1.txt $1_vul2.txt $1_vul3.txt | sort -u >> $1_js.txt
rm -rf "$1_vul1.txt"
rm -rf "$1_vul2.txt"
rm -rf "$1_vul3.txt"
#cat $1_js.txt | xargs -I% bash -c 'curl -sk "%" | grep -w "*.s3.us-east-2.amazonaws.com"' >> s3_bucket.txt
#cat $1_js.txt | xargs -I% bash -c 'curl -sk "%" | grep -w ".s3.us-east-2.amazonaws.com"' >> s3_bucket.txt
#cat $1_js.txt | xargs -I% bash -c 'curl -sk "%" | grep -w "s3.amazonaws.com/*"' >> s3_bucket.txt
#cat $1_js.txt | xargs -I% bash -c 'curl -sk "%" | grep -w "s3.us-east-2.amazonaws.com/*"' >> s3_bucket.txt
#cat $1_js.txt | xargs -I% bash -c 'curl -sk "%" | grep -w "amazonaws.com/*"' >> s3_bucket.txt
for URL in `cat $1_js.txt` ; do echo $URL ; curl "$URL" | grep amazonaws.com >> s3_bucket.txt ; done 
