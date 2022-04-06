#!usr/bin/python3
import subprocess  # by this we execute the commands , in unix shell
import re # importing regex expressions
import sys
# commands to change mac address manually
# ifconfig  eth0 down
# ifconfig eth0 hw ether new_mac
# ifconfig eth0 up
#dc:f5:05:a2:df:d5
#colors
import pyfiglet
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    B = "\033[0;34;40m" # Blue
    orange='\033[43m' 
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    pink='\033[95m'

ascii_banner = pyfiglet.figlet_format("MAC Proxy!!")
print(ascii_banner)
print(f"{bcolors.pink}Author: Viraj Vaishnav{bcolors.RESET}")
print(f"{bcolors.pink}Follow on: https://twitter.com/VirajVaishnav16{bcolors.RESET}")
def run():
     print(f"{bcolors.pink}what you want...{bcolors.RESET}")
     print(f"{bcolors.pink}1. check my mac.{bcolors.RESET}"+" "*18 + f"{bcolors.pink}2. change my mac.{bcolors.RESET}")
     option = input(f"{bcolors.pink}select option (1 0r 2): {bcolors.RESET}")
     if option == "1":
        iface = input(f"{bcolors.pink}which network card interface you want to check: {bcolors.RESET}{bcolors.lightred}")
        print(f"{bcolors.RESET}")
        mc = mac_changer()
        mc.get_mac(iface)
     else:
        iface = input(f"{bcolors.pink}which network card interface you want to check: {bcolors.RESET}{bcolors.lightred}")
        print(f"{bcolors.RESET}")
        new_mac = input(f"{bcolors.pink}new mac address you want to take: {bcolors.RESET}{bcolors.lightred}")
        print(f"{bcolors.RESET}")
        mc = mac_changer()
        mc.change_mac(iface,new_mac)
class mac_changer:
      def _init_(self):
         self.mac = ""
         
      def get_mac(self,iface):
          output = subprocess.run(["ifconfig",iface],shell=False,capture_output=True) # output is not a string it is a result of completed process, yaha par run ke ander jo list hai woh basically commands ke har uss word ko as a single element ko store krne ke liye hai jiske dono taraf space ho , basically word to word iss list mein elements store honge....
          result_string = output.stdout.decode('utf-8')
          #print(result_string)
          regex_pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
          regex = re.compile(regex_pattern)
          #print(regex)
          ans = regex.search(result_string) # here ans is also an opject you can check the object by printing it
          current_mac = ans.group().split(" ")[1]
          #print(ans)
          self.mac = current_mac
          #print("current MAC address for {} is {}".format(iface,current_mac))
          print(f"{bcolors.WARNING}current MAC address for {iface} is{bcolors.RESET} {bcolors.lightred}{current_mac}{bcolors.RESET}")
          run();
      def change_mac(self,iface,new_mac):
          # you will have to modify the appropritate configuration file under /etc/network/interfaces.d/ or the /etc/network/interfaces file itself if you want this change to always take effect at boot time. if you don't , your MAC address will be reset when you restart.
          output = subprocess.run(["ifconfig",iface,"down"],shell=False,capture_output=True)
          error = output.stderr.decode('utf-8')
          if len(error)!=0:
                print(error)
                sys.exit()
                
          output = subprocess.run(["ifconfig",iface,"hw","ether",new_mac],shell=False,capture_output=True)
          error = output.stderr.decode('utf-8')
          if len(error)!=0:
                print(error)
                sys.exit()
                
          output = subprocess.run(["ifconfig",iface,"up"],shell=False,capture_output=True)
          error = output.stderr.decode('utf-8')
          if len(error)!=0:
                print(error)
                sys.exit()
                
          run();
#program start from here...

run();
          
