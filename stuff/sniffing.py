#!/usr/bin/python3
from scapy.all import *
pkt = sniff(iface='wlan0',filter='icmp',count=10)
pkt.summary()
# iface='enp03' basically ek computer mein alag alag interface ho sakte hai,
# enp03,eth0,wlo0,etc in sab se alag alag ip address computer ko diye ja sakte hai,hence one computer can have more than one ip adress.
# different types of filter=
