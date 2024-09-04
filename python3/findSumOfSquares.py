import math
'''Find the sum of two squares that equal 36482'''

sum 	= 36482
#sum 	= 35377
sum = 41717
sum = 180
sum = 545000
sum = 610000
sum = 2101258
sum = 5353042
sum=34

sum = int(input('Enter an integer and I will find the sum of two squares that equal your Number: '))

found	= False

foundList = []

for x in range(1,1000000000+1):
	if x in foundList:
		continue
		
	y2 = sum - math.pow(x,2)

	if (y2 <= 0):
		break
	
	y = math.sqrt(y2)
	
	if (y - int(y) == 0):
		sum2 = math.pow(x,2)+ math.pow(y,2)
		if (sum2 == sum):
			print('Found it: {0} and {1:.0f}'.format(x,y))
			
			print('{0:.0f}^2 + {1:.0f}^2 = {2:.0f}'.format(x,y,sum2))
			
			foundList.append(int(y))
			#print(foundList)
		found = True
	#		break
	
if not found: 
	print('Not Found')
else:
	num = len(foundList)
	print(f'Found {num} occurences')
	
x2 = pow(x,2)
if (x2 > sum):
	print(f'Largest attempt was {x} since {x}^2 = {x2} > {sum}')
else:
	print(f'Largest attempt was {x}^2 = {x2}')
	
