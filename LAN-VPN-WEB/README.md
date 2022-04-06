# LAN-VPN-WEB
## Description
### this repository contains , different python3 scripts , which can be used to do various attacks within the subnet or on a real world web server. do not use it for any wrong purpose. if any harm caused by this scripts , then only users is responsible for it.

# Installation 
> git clone https://github.com/veer1024/LAN-VPN-WEB.git

> cd LAN-VPN-WEB/scripts/

> pip3 install -r requirements.txt


# Mac Proxy Tool
## **Description** 
### This Script is used to change the MAC Address of any Interface (wlan0, eth0 etc)
> python3 macproxy.py

![macproxy](https://user-images.githubusercontent.com/60743167/132130283-d9ad088c-ddea-42a3-914a-1f686a44c963.png)


# Network Mapper Tool
## **Description**
### This Script is used to list out all active hosts within a subnet , alogwith their IP and Mac Address.
> python3 networkrecord.py

![lan-mapper](https://user-images.githubusercontent.com/60743167/132130593-f8398b38-9ece-42e3-95ca-dfe64d52cbd4.png)

# MITM attacker
## **Description**
### This Script is used to perform man in the middle attack within the subnet , for this you need mac and IP addresses of both the machines for this you can use the below command 
> arp -a

### with this you can change tcp data (messages) , which target machines are sharing between them. to launch the script 
> python3 MITM.py

### and follow the steps mentioned in the below video to launch the attack.


https://user-images.githubusercontent.com/60743167/132137208-55dfe382-10a5-4e30-b39a-27c13a96d5ba.mp4

# TCP Session Hijacker or Telnet Session Hijacker
## **Description**
### This script is used to hijack telnet session between web server and client. this makes attacker to inject malicious code in the packets and to do remote code execution on Telnet server.
> python3 TCPsessionhijack.py

![tcp-session-hijacker](https://user-images.githubusercontent.com/60743167/132137629-afe305c3-7dab-4f37-8a2a-86ecbb17ff10.png)


# Domain Scanner 
## **Description**
### This script is used to do domain scan for Information Gathering and basic reccon . 
### Provide the path of file containing list of all domains or subdomains , and it will provide the following details
- Status code of all domains in form of table
- all domains vulnerable for clickjacking
- all domains vulnerable with cors
- check for some basic techniques for 403 bypass against all 403 domains
- check for domains having any header reflection

### to launch the attack
> python3 domain-scanner.py
> # provide the path of the file containing domains and subdomains.

![domain-scanner-1](https://user-images.githubusercontent.com/60743167/132132134-59d18cb9-be3a-4b48-8eef-c0e9c214e23a.png)

![domain-scanner-2](https://user-images.githubusercontent.com/60743167/132132289-908ea233-851b-4eed-b424-c4f1c7c0c88c.png)




