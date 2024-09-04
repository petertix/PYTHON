import random

random.seed()

coin = ['Heads', 'Tails']
Done = False
wrongCnt = 0

while not Done:
	flip = (input(''))
	result = random.choice(coin)
	
	if flip == '':
		guess = 'Heads'
		
	elif flip == ' ':
		guess = 'Tails'
		
	else:
		Done = True
		break
		
	print('Guess: ' + guess)
		
	print(" Flip: " + result)
	if result != guess:
		wrongCnt = wrongCnt + 1
		print('Wrong Count: ' + str(wrongCnt))
	else:
		wrongCnt = 0
		print('Wrong Count: ' + str(wrongCnt))
		
		
		
	
print('All Done!\n')