#!/usr/bin/python3
from scapy.all import *
def process_packet(pkt):
     #hexdump(pkt)
     pkt.show()
     #pkt.summary()
     print("---------------------------------------------------")
#hexdump() se jo bhi packet header and payload ka data milega woh  binary form mein hoga while ..show()  se milne wala data readable hoga
#f='udp and dst portrange 52-54 or icmp'
#f='udp and dst port 53'
f='icmp'
pkt = sniff(iface='wlo1',filter=f,prn=process_packet)
#pkt = sniff(iface='wlo1',filter='icmp',count=10)
#pkt = sniff(iface='wlo1',count=1,filter="tcp and host 64.233.167.99 and port 80")
