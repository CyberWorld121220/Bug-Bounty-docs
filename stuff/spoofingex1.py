#!/usr/bin/python3
from scapy.all import *
print("Sending SPOOFED ICMP packet...")
#targetmac="ff:ff:ff:ff:ff:ff"
fakemacforvictim="08:00:27:f9:64:17"
ether=Ether()
#ether.dst=targetmac
ether.src=fakemacforvictim
ip=IP(src="192.168.43.136",dst="8.8.8.8")
icmp=ICMP()
data='Y\x1c\x8a_\x00\x00\x00\x00\xd5o\x03\x00\x00\x00\x00\x00\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./01234567'
pkt=ether/ip/icmp/data
pkt.show()
sendp(pkt)
#send(pkt,verbose=0)
