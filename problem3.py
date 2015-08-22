limit = 600851475143
a = 2

while a*a <= limit:
	while limit% a == 0:
		limit = limit/a
	a = a + 1

print limit