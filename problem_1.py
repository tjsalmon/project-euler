total = 0
for n in range(0, 1000):
	if (n % 3 == 0 or n % 5 == 0): 
		total += n
print 'Sum of all multiples of 3 and 5 below 1000: {0}'.format(total)
