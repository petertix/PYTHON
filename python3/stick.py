'''
Break a stick in two places.
what is the probability that the 3 stick pieces
form a triangle?
Use Monte Carlo

---------n1---------n2----------
'''

import random
exps = int(input('Number of Experiments: '))

stickLen = 1000
triangle = 0
total = 0

for x in range(exps):
	n1 = random.randint(1,stickLen-1)
	n2 = random.randint(1,stickLen-1)
	
	if n1 > n2:
		save = n1
		n1 = n2
		n2 = save
		
	a = n1
	b = n2 - n1
	c = stickLen - n2
	
	if ( (a+b)>c and (a+c)>b and (b+c)>a ):
		triangle += 1
		
	total += 1
	
		
prob = float(triangle/total)

print('Probability of a triangle is: {}'.format(prob))

