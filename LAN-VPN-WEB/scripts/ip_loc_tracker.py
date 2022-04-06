#!usr/bin/python3
# in this we use api-ip (an api which provides inforamtion about the ip like,location,isp,and timezone etc, in json,xml and response forms...  , we can download the content of json file having info about the given ip using this api..,)
#https://ip-api.com/docs/api:json
# whenever we have to import modules from the any external api , we have to make a rquest and for that we have to install requests library to our environment which allows us to make a request to the external library.... and for installing requests in linux :: pip install requests
import requests
import json # because api gives info about api in json 
import argparse
from prettytable import PrettyTable
import pyfiglet
#colors
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

ascii_banner = pyfiglet.figlet_format("IP Locator !!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")

parser = argparse.ArgumentParser()
parser.add_argument("-i","--ipaddress",help="IP address to track") # now by this we added an help for the users,:: python3 ip_loc_tracker.py -h or python3 ip_loc_tracker.py --help to see the result..
args = parser.parse_args()
ip = args.ipaddress
#url = "http://ip-api.com/json/"+ip  # this gives default details
url = "http://ip-api.com/json/" + ip + "?fields=66846719"
# look like http://ip-api.com/json/192.168.43.1
response = requests.get(url)  # yein GET method hai ,jisse browser server se websites ki details leta hai...
# resposne ek json object hai hence ,
data = json.loads(response.content)  # here data is a dictinary containing data of json in key-value pair
#print(data)
print("\t[+] Status:\t\t\t",data["status"])
if data["status"] == "fail":
        print("\t[+] message:\t\t\t",data["message"])
else:
     table = PrettyTable(['info-Type', 'Value'])
     row1 = [bcolors.WARNING+"latitude"+bcolors.RESET,bcolors.lightred+str(data["lat"])+bcolors.RESET]
     row2 = [bcolors.WARNING+"longitude"+bcolors.RESET,bcolors.lightred+str(data["lon"])+bcolors.RESET]
     row3 = [bcolors.WARNING+"city"+bcolors.RESET,bcolors.lightred+data["city"]+bcolors.RESET]
     row4 = [bcolors.WARNING+"district"+bcolors.RESET,bcolors.lightred+data["district"]+bcolors.RESET]
     row5 = [bcolors.WARNING+"region"+bcolors.RESET,bcolors.lightred+data["region"]+bcolors.RESET]
     row6 = [bcolors.WARNING+"regionName"+bcolors.RESET,bcolors.lightred+data["regionName"]+bcolors.RESET]
     row7 = [bcolors.WARNING+"country"+bcolors.RESET,bcolors.lightred+data["country"]+bcolors.RESET]
     row8 = [bcolors.WARNING+"timezone"+bcolors.RESET,bcolors.lightred+data["timezone"]+bcolors.RESET]
     row9 = [bcolors.WARNING+"organization_name"+bcolors.RESET,bcolors.lightred+data["org"]+bcolors.RESET]
     row10 = [bcolors.WARNING+"ZIP Code"+bcolors.RESET,bcolors.lightred+str(data["zip"])+bcolors.RESET]
     row11 = [bcolors.WARNING+"Country Code"+bcolors.RESET,bcolors.lightred+str(data["countryCode"])+bcolors.RESET]
     row12 = [bcolors.WARNING+"ORGANIZATION"+bcolors.RESET,bcolors.lightred+data["as"]+bcolors.RESET]
     row13 = [bcolors.WARNING+"Reverse_DNS_of_IP"+bcolors.RESET,bcolors.lightred+data["reverse"]+bcolors.RESET]
     row14 = [bcolors.WARNING+"Cellular"+bcolors.RESET,bcolors.lightred+str(data["mobile"])+bcolors.RESET]
     row15 = [bcolors.WARNING+"VPN"+bcolors.RESET,bcolors.lightred+str(data["proxy"])+bcolors.RESET]
     row16 = [bcolors.WARNING+"Hosting"+bcolors.RESET,bcolors.lightred+str(data["hosting"])+bcolors.RESET]
     table.add_row(row1)
     table.add_row(row2)
     table.add_row(row3)
     table.add_row(row4)
     table.add_row(row5)
     table.add_row(row6)
     table.add_row(row7)
     table.add_row(row8)
     table.add_row(row9)
     table.add_row(row10)
     table.add_row(row11)
     table.add_row(row12)
     table.add_row(row13)
     table.add_row(row14)
     table.add_row(row15)
     table.add_row(row16)
     print(table)

# how to run : sudo ip_loc_tracker.py -i 192.168.43.1
