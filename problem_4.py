import math

palindrome = 1
for m in range(100, 1000):
	for n in range (100, 1000):
		num = m * n
		match = 0
		palin = str(num)
		for x in range(0,len(palin)/2):
			if (palin[x] == palin[(len(palin)-1)-x]):
				match += 1
			if (match >= (math.ceil(len(palin)-1)/2)):
				if (num > palindrome):
					palindrome = num
print 'The largest palindrome made from the product of two 3-digit numbers is {0} ({1} x {2}).'.format(palindrome,m,n)			
	
