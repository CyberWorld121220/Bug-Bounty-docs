import requests
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

ascii_banner = pyfiglet.figlet_format("Domain Status Code Checker !!")
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
   def __init__(self,domain,url,status):
          self.url = url
          self.status = status
          self.domain = domain
   def __repr__(self):
          thistuple = tuple((self.domain,self.url, self.status))
          return thistuple
   def taapu(self):
          tappu = tuple((self.domain,self.url, self.status))
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
                 domain_data = Domains(line.strip(),url,r.status_code)
                 result.append(domain_data.taapu())
                 print(f"{bcolors.OK}Target {count}: {line.strip()} ==>  {r.status_code}")
                 #print(domain_data.taapu())
                 r.close()
                 
            
    except Exception:
                url = 'https://'+line.strip()
                result.append(Domains(line.strip(),url,0).taapu())
                #print("Target {}: {} ==> {}".format(count,line.strip(),"no domain found"))
                print(f"{bcolors.FAIL}Target {count}: {line.strip()} ==>  no domain found")
 
result.sort(key=get_my_key)            # sorting
result = list(dict.fromkeys(result))   # removing duplicating   



# removing duplicates


print(bcolors.RESET)
table = PrettyTable(['Domain', 'URL', 'Status Code'])
table_fail = PrettyTable(['Domain', 'URL', 'Status Code'])
for rec in result:
    if rec[2] !=0:
          if rec[2] < 300:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.pink+str(rec[2])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
          elif rec[2] < 400:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.orange+str(rec[2])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
          elif rec[2] < 500:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.lightred+str(rec[2])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
          else:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.lightgrey+str(rec[2])+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table.add_row(row)
    else:
              row = [bcolors.B+rec[0]+bcolors.RESET,bcolors.B+str(rec[1])+bcolors.RESET,bcolors.FAIL+"Domain not found!!"+bcolors.RESET]     # row must be a list , we can't pass Domains object as a list
              table_fail.add_row(row)
    
print(table)
print(table_fail)
