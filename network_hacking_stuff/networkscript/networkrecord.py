#!usr/bin/python3
from scapy.all import *
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
        print("IP"+" "*18 + "MAC")
        for Host in Hosts: 
               print("{:16}   {}".format(Host['IP'],Host['mac']))
def Mapper(pkt):
      print("all hosts on the network are mapped below as IP_ADDRESS :: MAC_ADDRESS")
      print("   {} :: {}".format(pkt[IP].src,pkt[Ether].src))
      
      

targetMAC = input("Target MAC:")
target = input("Target Subnet (CIDR_NOTATION or IP_ADDRESS):")
print("====================MAPPER=====================")
sendingarprequest();

        
