#!/bin/bash
output=$1
python3 param_replacer.py -l "${output}/${output}xssurls.txt"
filename="${output}/${output}xssurls_reflect.txt"
while read -r line; do
    name="$line"
    #echo "Name read from file - $name"
    reflect=$(curl -f --silent $name 2>&1 | grep viraj)
    #echo "${#reflect}"
    if [ ${#reflect} -gt 1 ];
    then
    echo "${name}" >> "${output}/${output}_reflecting_param.txt"
    else
    echo "No Reflection found"
    fi
done < "$filename"
rm -rf "${filename}"

