G = input("Enter G value (in hex: 0x...): ")
G = bin(int(G, 16))[2:].zfill(8)

A = "01100000" # binary for 96
B = "00000011" # binary for 3

x = ""
y = ""
# XOR solver
for i in range(0, len(G)):
	if G[i] == A[i]:
		x = x + '0'
	else:
		x = x + '1'

for i in range(0, len(G)):
	if G[i] == B[i]:
		y = y + '0'
	else:
		y = y + '1'

x = chr(int(x, 2))
y = chr(int(y, 2))
print(x*3 + y)
