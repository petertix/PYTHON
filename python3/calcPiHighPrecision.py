'''
Calculate pi with the formula:
	pi = 2 + 1/3(2+2/5(2+k/(2k+1)))
	Peter: Aug 21, 2021
'''
from decimal import Decimal, getcontext
import math
#import mpmath

try:
	# import version included with old SymPy
	from sympy.mpmath import mp
except ImportError:
	# import newer version
	from mpmath import mp

getcontext().prec = 31
mp.dps = 31  # set number of digits



n = input('Enter an integer k: ')
n = int(n)

mypi = 1
for k in range(n,0,-1):
	mypi = 2 + mypi*( Decimal(k)/(2*Decimal(k)+ 1))
	
	print('pi[{0:5d}] = {1:.30f}'.format(n-k+1,mypi))
	


#print(mp.pi)   # print pi to a thousand places

print('pi[{0:5s}] = {1}'.format('Math',mp.pi))

a = float(Decimal(mypi))
b = float(mp.pi)

print('pi[{0:5s}] = {1:.30f}'.format('Diff', abs(a-b)))