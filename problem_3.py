import math

num = input('Please enter a number: ')
product = 1
for n in range(2,math.trunc(math.sqrt(num))):
	if (num % n == 0):
#		print n
		product *= n
		if (product == num):
			print 'Largest prime factor of {0}: {1}'.format(num,n)
			break
