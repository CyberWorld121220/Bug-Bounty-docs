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

ascii_banner = pyfiglet.figlet_format("URL Capturer!!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
target = input("Enter the target: ")
