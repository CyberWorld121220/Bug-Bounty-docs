#!/bin/bash
cat "${2}urls.txt" | subjs >> "${2}js.txt"
cat "${2}urls.txt" "${2}js.txt" | sort -u >> ${2}_totalurls.txt
while IFS= read -r line;
do
  #echo "$line"
  curlresult=$(curl -v "${line}" | grep s3.amazonaws.com 2>/dev/null)
  if [ ${#curlresult} -gt 10 ];then
  echo "$line" >> "TestingData/${1}/${2}/${2}awsurls.txt"
  fi
done < "${2}_totalurls.txt"
rm -rf "${2}js.txt"
rm -rf "${2}_totalurls.txt"
