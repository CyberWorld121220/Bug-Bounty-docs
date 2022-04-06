#!usr/bin/python3
# in this we use api-ip (an api which provides inforamtion about the ip like,location,isp,and timezone etc, in json,xml and response forms...  , we can download the content of json file having info about the given ip using this api..,)
#https://ip-api.com/docs/api:json
# whenever we have to import modules from the any external api , we have to make a rquest and for that we have to install requests library to our environment which allows us to make a request to the external library.... and for installing requests in linux :: pip install requests
import requests
import json # because api gives info about api in json 
import argparse


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
     print("\t[+] IP\t\t\t",data["query"])
     #location based data: 
     print("location data:")
     print("\t[+] latitude\t\t\t",data["lat"])
     print("\t[+] longitude\t\t\t",data["lon"])
     print("\t[+] city\t\t\t",data["city"])
     print("\t[+] district\t\t\t",data["district"])
     print("\t[+] region\t\t\t",data["region"])
     print("\t[+] regionName\t\t\t",data["regionName"])
     print("\t[+] country\t\t\t",data["country"])
     print("\t[+] timezone:\t\t\t",data["timezone"])
     print("\t[+] organization_name\t\t\t",data["org"])
     print("\t[+] ZIP code\t\t\t",data["zip"])
     print("\t[+] COUNTRY_code\t\t\t",data["countryCode"])
     # some other details:
     print("some other important details:")
     print("\t[+] ORGANIZATION\t\t\t",data["as"])
     print("\t[+] Reverse_DNS_of_IP:\t\t\t",data["reverse"])
     print("\t[+] Cellular\t\t\t",data["mobile"])
     print("\t[+] VPN\t\t\t",data["proxy"])
     print("\t[+] hosting\t\t\t",data["hosting"])
     

# how to run : sudo ip_loc_tracker.py -i 192.168.43.1
