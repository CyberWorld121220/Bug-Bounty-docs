#!usr/bin/python3
import subprocess  # by this we execute the commands , in unix shell
import re # importing regex expressions
import sys
# commands to change mac address manually
# ifconfig  eth0 down
# ifconfig eth0 hw ether new_mac
# ifconfig eth0 up
#dc:f5:05:a2:df:d5
def run():
     print("what you want...")
     print("1. check my mac."+" "*18 + "2. change my mac.")
     option = input("select option (1 0r 2): ")
     if option == "1":
        iface = input("which network card interface you want to check: ")
        mc = mac_changer()
        mc.get_mac(iface)
     else:
        iface = input("which network card interface you want to check: ")
        new_mac = input("new mac address you want to take: ")
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
          print("current MAC address for {} is {}".format(iface,current_mac))
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
          
