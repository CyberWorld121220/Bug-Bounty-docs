import pwn

with open('cipher.txt','r') as handler:
    cipher = handler.read()
    
    # cipher = cipher.decode('base64')
    for i in range(256):
       message = pwn.xor(cipher,i)
       print message
       
##################################### generating permuutation of 4 char lowercase string ###########################
from string import *
from itertools import permutations

string = list(ascii_lowercase)

perm = permutations(string,4)

for i in perm:
   print("".join(i))
