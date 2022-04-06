#!/usr/bin/pyhton3
from scapy.all import *
print("Sending Spoofed Packets.....")
ip=IP(src="192.168.43.246",dst="192.168.43.244")
udp=UDP(sport=9090,dport=9090)
data="HEllo BHAI!\n"
pkt=ip/udp/data
pkt.show()
send(pkt,verbose=0)
