import math

def calcPi(n):
	
	pi = 0
	for x in range(n):
		if (x % 2) == 0:
			one = 1
		else:
			one = -1
		
		pi += 4*one / (2*x + 1)
		
	return(pi)
	


if __name__ == "__main__":
	
	n = int(input('Enter n: '))
	
	print(calcPi(n))