#!usr/bin/python3
from scapy.all import *
import pyfiglet
from prettytable import PrettyTable
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

ascii_banner = pyfiglet.figlet_format("LAN Mapper!!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
def sendingarprequest():
        ether=Ether()
        ether.dst=targetMAC
        arp=ARP()
        arp.pdst=target
        arp.op=1
        frame=ether/arp
        resultlist = srp(frame,timeout=3,verbose=0)[0]   # sending an arp response  // srp function basically ek list generate krta hai ,              #packet_received_by_host:packet_sent_by_host
        
        Hosts = []
        for sent,received in resultlist: 
             # for each response ,append ip and mac address to 'Hosts' list
             Hosts.append({'IP':received.psrc,'mac':received.hwsrc})
        #printing hosts:
        print("Available devices in the network...")
        table = PrettyTable(['IP', 'MAC'])
        #print("IP"+" "*18 + "MAC")
        for Host in Hosts:
               row = [bcolors.lightred+Host['IP']+bcolors.RESET,bcolors.WARNING+Host['mac']+bcolors.RESET]
               table.add_row(row) 
               #print("{:16}   {}".format(Host['IP'],Host['mac']))
        print(table)
def Mapper(pkt):
      print("all hosts on the network are mapped below as IP_ADDRESS :: MAC_ADDRESS")
      print("   {} :: {}".format(pkt[IP].src,pkt[Ether].src))
      
      

targetMAC = input(f"{bcolors.WARNING}MAC To Set(Set by your choice,whatever you want to use):{bcolors.RESET}{bcolors.lightred}")
print(f"{bcolors.RESET}")
target = input(f"{bcolors.WARNING}Target Subnet (CIDR_NOTATION or IP_ADDRESS):{bcolors.RESET}{bcolors.lightred}")
print(f"{bcolors.RESET}")
print("====================MAPPER=====================")
sendingarprequest();

        
