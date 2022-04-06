#!/bin/bash
while getopts t:f:o: flag
do
    case "${flag}" in
        t) target=${OPTARG};;
        f) targetfile=${OPTARG};;
        o) output=${OPTARG};;
    esac
done
mkdir $output
if [ ${#targetfile} -gt 1 ];
then
gau -subs $target;cat $targetfile | waybackurls | sort -u >> "${output}urls.txt" | mv "${output}urls.txt" ./"${output}"/
else
gau -subs $target; subfinder -d $target -silent |waybackurls | sort -u >> "${output}urls.txt" | mv "${output}urls.txt" ./"${output}"/
fi
cd "${output}"
cat "${output}urls.txt" | gf ssrf | sort -u >> "${output}ssrfurls.txt"
cat "${output}urls.txt" | gf redirect | sort -u >> "${output}redirecturls.txt"
cat "${output}urls.txt" | gf sqli | sort -u >> "${output}sqliurls.txt"
cat "${output}urls.txt" | gf s3-buckets | sort -u >> "${output}s3urls.txt"
cat "${output}urls.txt" | gf idor | sort -u >> "${output}idorurls.txt"
cat "${output}urls.txt" | gf xss | sort -u >> "${output}xssurls.txt"
cat "${output}urls.txt" | gf rce | sort -u >> "${output}rceurls.txt"
cat "${output}urls.txt" | gf wp | sort -u >> "${output}wpurls.txt"
