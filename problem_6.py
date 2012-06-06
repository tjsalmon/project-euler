import math
sumofsquares = 0
squareofsum = 0

for i in range(1,101):
	sumofsquares += pow(i,2)

for j in range(1,101):
	squareofsum += j
squareofsum = pow(squareofsum,2)

print 'The difference between the sum of squares and square of sums from 1-100 is: {0}'.format(squareofsum - sumofsquares)

