#!/bin/bash
echo "Usage => urltest.sh -t target -f targetsubdomainsfile -o output"
while getopts t:f:g:o: flag
do
    case "${flag}" in
        t) target=${OPTARG};;
        f) targetfile=${OPTARG};;
        g) gauonly=${OPTARG};;
        o) output=${OPTARG};;
    esac
done
Var="$gauonly"
if [ -z "$gauonly" ];
then
Var="No"
else
echo "OK"
fi
if [ $Var  == "yes" ];
then
gau -subs $target | sort -u >> "${output}urls.txt"
echo "Gau URL exploration Completed"
else
if [ ${#targetfile} -gt 1 ];
then
gau -subs $target;cat $targetfile | waybackurls | sort -u >> "${output}urls.txt"
echo " ............ "
echo " URL exploration done ......"
else
gau -subs $target; subfinder -d $target -silent | waybackurls | sort -u >> "${output}urls.txt"
fi
fi
echo "Creating directory"
mkdir $output
echo "Moving ${output}urls.txt to directory ${output} ..."
mv "${output}urls.txt" ./"${output}"/
echo "Going to Directory ${output}"
cd "${output}"
cat "${output}urls.txt" | gf ssrf | sort -u >> "${output}ssrfurls.txt"
cat "${output}urls.txt" | gf redirect | sort -u >> "${output}redirecturls.txt"
cat "${output}urls.txt" | gf sqli | sort -u >> "${output}sqliurls.txt"
cat "${output}urls.txt" | gf s3-buckets | sort -u >> "${output}s3urls.txt"
cat "${output}urls.txt" | gf idor | sort -u >> "${output}idorurls.txt"
cat "${output}urls.txt" | gf xss | sort -u >> "${output}xssurls.txt"
cat "${output}urls.txt" | gf rce | sort -u >> "${output}rceurls.txt"
cat "${output}urls.txt" | gf wp | sort -u >> "${output}wpurls.txt"
cat "${output}urls.txt" | gf auth | sort -u >> "${output}authurls.txt"
