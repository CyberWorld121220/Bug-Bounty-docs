#!/bin/bash
IFS='.' read -ra ADDR <<< "$1"
blogalternate=${ADDR[0]}
while IFS= read -r line; do
status=$(curl -s -o /dev/null -I -w "%{http_code}" 'http://'$line'.s3.amazonaws.com')
if [ ${#status} -gt 0 ] && [ $status != "404" ]; then
echo $line >> "TestingData/${1}/${2}_aws_buckets.txt"
fi
wp_status=$(curl -s -o /dev/null -I -w "%{http_code}" 'https://'$line'/xmlrpc.php')
#echo "for $line : wp_status is : $wp_status"
wp_stauts_2=$(curl -s -o /dev/null -I -w "%{http_code}" 'https://'$line'/blog/xmlrpc.php')
#echo "for $line : wp_status is : $wp_status_2"
wp_stauts_3=$(curl -s -o /dev/null -I -w "%{http_code}" 'https://'$line'/'$blogalternate'/xmlrpc.php')
#echo "for $line : wp_status is : $wp_status_3"
if [ ${#wp_status} -gt 0 ]; then if [ $wp_status == "405" ];then
echo 'https://'$line'/xmlrpc.php' >> "TestingData/${1}/${2}_wordpress.txt"
fi
elif [ ${#wp_status_2} -gt 0 ]; then if [ $wp_status_2 == "405" ];then
echo 'https://'$line'/blog/xmlrpc.php' >> "TestingData/${1}/${2}_wordpress.txt"
fi
elif [ ${#wp_status_3} -gt 0 ];then if [ $wp_status_3 == "405" ];then
echo 'https://'$line'/'$blogalternate'/xmlrpc.php' >> "TestingData/${1}/${2}_wordpress.txt"
fi
fi
#urls[$i]=$line;
#i=$((i + 1))
done < "${2}_subdomains.txt"
