def palindrome(number):
	if str(number)[::-1] == str(number):
		return True
	else:
		return False

cap = 1000
a = 1000
b = 999
biggest_pali = 0

while a >= 0:
	a -= 1
	for i in range(a, cap):
		b = i
		if palindrome(a*b) == True:
			if a * b > biggest_pali:
				biggest_pali = a * b
	if a * 999 < biggest_pali:
		break

print biggest_pali