#every number below half doesn't need to be checked
#our number has to be a multiple of 2520
#2520 is also already evenly divisible by 20 18 15 14 12
i = 1
a = 2520
found = False


while found == False:
	b = i * a
	if b % 19 == 0 and b % 17 == 0 and b % 16 == 0 and b % 13 == 0 and b % 11 == 0:
		print b
		found = True
		break
	i += 1