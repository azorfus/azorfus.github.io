import socket
import struct

handle = socket.socket()
connect = handle.connect(("vortex.labs.overthewire.org", 5842))

s = 0
for i in range(0, 4):
	# One unsigned integer is 4 bytes big
	s = s + int(struct.unpack("I", handle.recv(4))[0])

handle.send(struct.pack("I", s))
print(handle.recv(1024))
