#!/usr/bin/python3
from scapy.all import *
# yaha par jo pkt hai woh basically capture kiya hua packet hai
def process_packet(pkt):
   if pkt.haslayer(IP):
       # condition ka mtlb hai ke IP datagram wala section present hai ya nahi data packet ke ander
       ip=pkt[IP]
       if pkt.haslayer(TCP):
          tcp=pkt[TCP]
          if pkt.haslayer(Raw):
            data=pkt[Raw].load
            print("data inside the packet:",data)
            print("TCP Ports: src {} --> des {}".format(tcp.sport,tcp.dport))
            print("IP: src {} --> des {}".format(ip.src,ip.dst))
       elif pkt.haslayer(UDP):
          udp=pkt[UDP]
          if pkt.haslayer(Raw):
            data=pkt[Raw].load
            print("data inside the packet:",data)
            print("UDP Ports: src {} --> des {}".format(udp.sport,udp.dport))
            print("IP: src {} --> des {}".format(ip.src,ip.dst))
       else:
          print("Nothing else is found inside the packet...")
   elif pkt.haslayer(ICMP):
         # condition ka mtlb hai ke IP datagram wala section present hai ya nahi data packet ke ander
         icmp=pkt[ICMP]
         print("ICMP:TYPE  {}".format(icmp.type))
   else:
        print("Protocol not determined...")

#yein sniff wali line hi packet capture kr rahi hai...
f='udp and dst portrange 9089-9091 or tcp'
#sniff(iface="wlo1",filter='ip',prn=process_packet)
sniff(iface="wlo1",filter=f,prn=process_packet)

