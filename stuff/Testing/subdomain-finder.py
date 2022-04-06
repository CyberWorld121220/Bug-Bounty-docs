import subprocess  # by this we execute the commands , in unix shell
import re # importing regex expressions
import sys
import pyfiglet
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    B = "\033[0;34;40m" # Blue
    orange='\033[43m' 
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    pink='\033[95m'

ascii_banner = pyfiglet.figlet_format("Subdomain Finder!!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
target = input("Enter the target: ")

x = target.split(".")
regex_string = "[\dA-Za-z-]+(\W)"+target+"(|\W)"
regex = re.compile(regex_string)
## extracting Subdomains using subfinder,assetfinder,sublist3r , amass.
#print(regex_string)

## list of subdomains
subdomains = list()

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
    subdomains.append(match_obj.group())
#print(regex_string)
subdomains = list(dict.fromkeys(subdomains))
subdomain=open('subdomains.txt','w')
for element in subdomains:
    #print >>subdomain, element
    subdomain.write(element)
    subdomain.write('\n')
subdomain.close()
assetfinder = subprocess.run(["assetfinder","--subs-only",target],shell=False,capture_output=True) ## assetfinder
result_assetfinder = assetfinder.stdout.decode('utf-8')
#print(result_subfinder)
ans = regex.finditer(result_assetfinder)
for match_obj in ans:
    # print each re.Match object
    #print(match_obj)
    
    # extract each matching number
    print(match_obj.group())
    subdomains = subdomains.append(match_obj.group())
    subdomain = open('subdomains.txt','w')
    #print >>subdomain, match_obj.group()
    subdomain.write(match_obj.group())
    subdomain.write('\n')
    subdomain.close()
#print(regex_string)
subdomains = list(dict.fromkeys(subdomains))
## extracting Subdomains using subfinder,assetfinder,sublist3r , amass.
sublist3r = subprocess.run(["python3","sublist3r.py","-d",target],shell=False,capture_output=True) ## sublist3r
result_sublist3r = sublist3r.stdout.decode('utf-8')
#print(result_subfinder)
ans = regex.finditer(result_sublist3r)
for match_obj in ans:
    # print each re.Match object
    #print(match_obj)
    
    # extract each matching number
    print(match_obj.group())
    subdomains = subdomains.append(match_obj.group())
    subdomain = open('subdomains.txt','w')
    #print >>subdomain, match_obj.group()
    subdomain.write(match_obj.group())
    subdomain.write('\n')
    subdomain.close()
subdomains = list(dict.fromkeys(subdomains))
## extracting Subdomains using subfinder,assetfinder,sublist3r , amass.
amass = subprocess.run(["amass","enum","-d",target],shell=False,capture_output=True) ## amass
result_amass = amass.stdout.decode('utf-8')
#print(result_subfinder)
ans = regex.finditer(result_amass)
for match_obj in ans:
    # print each re.Match object
    #print(match_obj)
    
    # extract each matching number
    print(match_obj.group())
    subdomains = subdomains.append(match_obj.group())
    subdomain = open('subdomains.txt','w')
    #print >>subdomain, match_obj.group()
    subdomain.write(match_obj.group())
    subdomain.write('\n')
    subdomain.close()
#print(regex_string)
subdomains = list(dict.fromkeys(subdomains))


