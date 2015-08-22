a = 1
b = 2
counter = 2

while a + b < 4000000:
	a = a + b
	if a % 2 == 0:
		counter += a
	b = b + a
	if b % 2 == 0:
		counter += b

print counter