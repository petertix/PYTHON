import random

random.seed()

thing = ['Rose', 'Watch', 'Shoe', 'Bottle', 'Card','Plate', 'Newspaper', 'Phone', 'Gloves', 'Hat', 'Candle', 'Glass']

effect = ['Production', 'Vanish', 'Attraction', 'Prediction', 'Levitation', 'Transformation', 'Animation', 'Mentalism', 'Restoration', 'Penetration', 'Transportation', 'Transposition']

method = ['Magnets', 'Well', 'Duplicate', 'Shell', 'Black Art', 'Thread', 'Stealing', 'Pull/Thread', 'Misdirection', 'Switch', 'Topit', 'servante']

Done = False
wrongCnt = 0

print('Press the return key...')
while not Done:
	go = (input(''))
	if go == 99:
		Done = true
	myObject = random.choice(thing)
	myEffect = random.choice(effect)
	myMethod = random.choice(method)
		
	print('Object: ' + myObject + '\nEffect: ' + myEffect + '\nMethod: ' + myMethod)
		
	
print('All Done!\n')