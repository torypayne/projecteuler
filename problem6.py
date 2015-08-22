sum_of_squares = 0
for i in xrange(101):
	sum_of_squares += i*i

square_of_sums = sum(xrange(101)) * sum(xrange(101))

print square_of_sums - sum_of_squares

#if in python 3 you'd obvs need to use range instead of xrange