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
ascii_banner = pyfiglet.figlet_format("Similar Element Remover !!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
a = input(f"{bcolors.lightred}Path of target File:{bcolors.RESET} ")
file = open(a,'r')
Lines = file.readlines()
count = 0
list_domain = list()
for line in Lines:
       list_domain.append(line.strip())
result = list(dict.fromkeys(list_domain))   # removing duplicating 
for l in result:
     f = open("SR-"+a, "a")
     f.writelines(l+"\n")
     f.close()
print(f"{bcolors.pink}New File is created with SR-target-file-name.txt name{bcolors.RESET}")
