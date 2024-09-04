'''
Calculate pi with the formula:
	pi = 2 + 1/3(2+2/5(2+k/(2k+1)))
'''

import math
try:
	# import version included with old SymPy
	from sympy.mpmath import mp
except ImportError:
	# import newer version
	from mpmath import mp

mp.dps = 17  # set number of digits

#n = input('Enter an integer k: ')
#n = int(n)
n=100000

z = input('Enter an integer z: ')
z = int(z)

for a in range(1,z+1):
	mypi = 1
	for k in range(n,0,-1):
		mypi = a + mypi*( k/(a*k + 1))
	
	print('pi[{0:4d}] = {1:.16f}'.format(a,mypi))
	


#print(mp.pi)   # print pi to a thousand places

#print('pi[{0:5s}] = {1}'.format('Math',mp.pi))

#print('pi[{0:5s}] = {1:.18f}'.format('Diff', abs(float(mypi-mp.pi))))