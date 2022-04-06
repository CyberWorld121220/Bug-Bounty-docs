#!usr/bin/python3
import subprocess  # by this we execute the commands , in unix shell
import re # importing regex expressions
import sys
target = input("Enter the target: ")

x = target.split(".")
regex_string = "[\dA-Za-z-]+(\W)"+target+"(|\W)"
regex = re.compile(regex_string)
#print(regex_string)

## extracting Subdomains using subfinder,assetfinder,sublist3r , amass.
subfinder = subprocess.run(["subfinder","-d",target],shell=False,capture_output=True) ## subfinder
result_subfinder = subfinder.stdout.decode('utf-8')
#print(result_subfinder)
ans = regex.finditer(result_subfinder)
for match_obj in ans:
    # print each re.Match object
    #print(match_obj)
    
    # extract each matching number
    print(match_obj.group())
