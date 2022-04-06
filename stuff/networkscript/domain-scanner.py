import requests
import re
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

ascii_banner = pyfiglet.figlet_format("Domain Scanner!!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
a = input(f"{bcolors.lightred}Path of target File:{bcolors.RESET} ")
file = open(a,'r')
Lines = file.readlines()
count = 0
result = list()
#definig class for list 
class Domains:
   def __init__(self,domain,url,status,reason):
          self.url = url
          self.status = status
          self.domain = domain
          self.reason = reason
   def __repr__(self):
          thistuple = tuple((self.domain,self.url, self.status,self.reason))
          return thistuple
   def taapu(self):
          tappu = tuple((self.domain,self.url, self.status,self.reason))
          return tappu


def get_my_key(obj):
  return obj[2]
# reading each domain
for line in Lines:
    count  +=1
    try:     
                 s = requests.Session()
                 url = 'https://'+line.strip()
                 r = s.get(url)
                 domain_data = Domains(line.strip(),url,r.status_code,r.reason)
                 result.append(domain_data.taapu())
                 print(f"{bcolors.OK}Target {count}: {line.strip()} ==>  {r.status_code}")
                 #print(domain_data.taapu())
                 r.close()
                 
            
    except Exception:
                url = 'https://'+line.strip()
                result.append(Domains(line.strip(),url,0,"no response").taapu())
                #print("Target {}: {} ==> {}".format(count,line.strip(),"no domain found"))
                print(f"{bcolors.FAIL}Target {count}: {line.strip()} ==>  no domain found")
 
result.sort(key=get_my_key)            # sorting
result = list(dict.fromkeys(result))   # removing duplicating   



# Declaring lists for further refrence:
list404 = list()
list403 = list()
list302 = list()
list200 = list()


print(bcolors.RESET)
table = PrettyTable(['Domain', 'url', 'Status Code','Server Said'])
table_fail = PrettyTable(['Domain', 'url', 'Status Code','Server Said'])
for rec in result:
    if rec[2] !=0:
          if rec[2] < 300:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.pink+str(rec[2])+bcolors.RESET,bcolors.pink+str(rec[3])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
              list200.append(rec)
          elif rec[2] < 400:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.orange+str(rec[2])+bcolors.RESET,bcolors.pink+str(rec[3])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
              list302.append(rec)
          elif rec[2] < 500:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.lightred+str(rec[2])+bcolors.RESET,bcolors.pink+str(rec[3])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
              if rec[2] == 404:
                  list404.append(rec)
              else:
                  list403.append(rec)
          else:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.lightgrey+str(rec[2])+bcolors.RESET,bcolors.pink+str(rec[3])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
    else:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.FAIL+"Domain not found!!"+bcolors.RESET,bcolors.pink+str(rec[3])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table_fail.add_row(row)
    
print(table)
print(table_fail)
#print(list200)
#print(list302)
#print(list404)
#print(list403)

# ClickJacking 
list_c = list200 + list302
print(f"{bcolors.B}"+" Pages Vulnerable for ClickJacking Attacks..."+f"{bcolors.RESET}")
for domain in list_c:
     s = requests.session()
     url = domain[1]
     r = s.get(url)
     x = str(r.headers)
     R = re.search("X-Frame-Options", x)
     if R != None:
         print(f"{bcolors.FAIL} [+]"+url+f"{bcolors.RESET}")
# Header Reflection
list_h = list200 + list302 + list403
print(f"{bcolors.B}"+" Header Reflection......."+f"{bcolors.RESET}")
for domain in list_h:
     s = requests.session()
     url = domain[1]
     r1 = s.get(url,headers={'X-Forwarded-Host': 'evil.com'})
     r2 = s.get(url,headers={'X-Host': 'evil.com'})
     r3 = s.get(url,headers={'Host': 'https://evil.com','Cookie': 'evil :viraj'})
     r4 = s.get(url,headers={'Cookie': 'evil.com :viraj'})
     x1 = str(r1.headers)
     x1a = str(r1.text)
     x1b = str(r2.text)
     x1c = str(r3.text)
     x1d = str(r4.text)
     x2 = str(r2.headers)
     x3 = str(r3.headers)
     x4 = str(r4.headers)
     R1 = re.search("evil",x1)
     R2 = re.search("evil",x2)
     R3 = re.search("evil",x3)
     R4 = re.search("evil",x4)
     R1a = re.search("evil",x1a)
     R1b = re.search("evil",x1b)
     R1c = re.search("evil",x1c)
     R1d = re.search("evil",x1d)
     if R1 != None or R2 != None or R3 != None or R4 != None or R1a != None or R1b != None or R1c != None or R1d != None:
             print(f"{bcolors.B}"+url+f"{bcolors.RESET}")


# 403 forbidden bypass:
print(f"{bcolors.B}"+" 403 Bypass......."+f"{bcolors.RESET}")
table_403bypass = PrettyTable(['Domain', 'url', 'Payload','status','Server Said'])
for domain in list403:
       # Test 1 , GET => POST
       s = requests.session()
       url = domain[1]
       custom_header = {"Content-Length": "0"}
       r = s.post(url,headers = custom_header)
       if r.status_code != 403 and r.status_code != 404:
          row =  [bcolors.B+domain[0]+bcolors.RESET,bcolors.B+str(domain[1])+bcolors.RESET,bcolors.pink+str(custom_header)+bcolors.RESET,bcolors.pink+str(r.status_code)+bcolors.RESET,bcolors.orange+r.reason+bcolors.RESET] 
          table_403bypass.add_row(row)
       r.close()
       # Test 2 applying parameter
       url = domain[1] + "FUZZ"
       list = ["/.css","/?.css","/.svg","/?.svg","/.png","/?.png","//","/%20/","/%2e/","/.../","/./","?css","?.css","/.;/","#"]
       for l in list:
           url = url.replace("FUZZ",l)
           s = requests.session()
           r = s.get(url)
           if r.status_code != 403 and r.status_code != 404:
               row =  [bcolors.B+domain[0]+bcolors.RESET,bcolors.B+str(domain[1])+bcolors.RESET,bcolors.pink+url+bcolors.RESET,bcolors.pink+str(r.status_code)+bcolors.RESET,bcolors.orange+r.reason+bcolors.RESET] 
               table_403bypass.add_row(row)
           r.close()
           url = domain[1] + "FUZZ"
print(table_403bypass)
print(f"{bcolors.B}"+" Text Injection......."+f"{bcolors.RESET}")
# Reflection for Test Injection:
table_text_injection = PrettyTable(['Domain', 'url','status'])
list_reflection = list403 + list404
for domain in list403:
      s = requests.session()
      url = domain[1] + "/Viraj"
      r = s.get(url)
      R = re.search("Viraj",str(r.text))
      if  R != None:
           print(f"{bcolors.OK}Vulnerable Page: {url} ==>  {r.status_code}")
      r.close()  
     
