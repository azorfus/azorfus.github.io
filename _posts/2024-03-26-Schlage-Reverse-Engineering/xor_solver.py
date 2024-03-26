print("x^B = C")
b = str(input("Enter B: "))
c = str(input("Enter C: "))
x = ""

'''
| A | B | A XOR B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |
'''

for i in range(0, len(b)):
	if b[i] == c[i]:
		x = x + '0'
	else:
		x = x + '1'

print("X:", x)
