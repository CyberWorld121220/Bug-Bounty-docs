#!/usr/bin/python3
from scapy.all import *
#first fragment
udp = UDP(sport=12345,dport=12345,chksum=0)
udp.len = 8 + 32 + 40 + 20
ip = IP(dst="192.168.43.246",id=1000,frag=0,flags=1)
payload="A"*31 + "\n"
packet = ip/udp/payload   # during fragmentation udp and payload ko ek single payload mankar ip fragmentation hota hai.. # udp packet 8byte and payload 32 byte total
# 40 byte mtlb , next fragment ke liye frag 40/8  = 5 set krna hai
#sendp(packet) 
send(packet,verbose=0) 
#second fragment
ip = IP(dst="192.168.43.246",id=1000,frag=5,flags=1)
ip.proto = 17 # har bar ek udp packet banane ki zarurat nhi hoti ,ip.proto = 17 mtlb udp and 6 mtlb tcp
payload = "A"*39 + "\n" #last packet mein ,frag = 5 mtlb 5*8 = 40 byte and last packet mein ip payload h=jo hai woh 40byte ka mtlb #total 80 byte toh next #fragmented packet ka frag value will 80/8 = 10
packet = ip/payload 
#sendp(packet)
send(packet,verbose=0)
#third fragment 
ip = IP(dst="192.168.43.246",id=1000,frag=10,flags=0) # flags  = 0 mtlb yein last fragmented packet hai
ip.proto = 17
payload = "F"*19 + "\n"
packet= ip/payload
#sendp(packet)
send(packet,verbose=0)
