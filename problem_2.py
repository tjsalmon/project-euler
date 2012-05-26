total = 0
n = 0
n1 = 0
n2 = 1
while n < 4000000:
	n = n1 + n2
	n1 = n2
	n2 = n
	if n % 2 == 0: 
		total += n
print 'Sum of even-valued terms less than 4 million in Fibonacci sequence: {0} '.format(total)

