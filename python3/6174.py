import sys

def calcSpecialNum(myNum):
	myLen = len(myNum)
	
	s=[str(x) for x in myNum]
	
	s.sort()
	myMin=int(''.join(s))
	s.reverse()
	myMax=int(''.join(s))
	
	return(str(myMax - myMin))
	
	


while(True):
   myNum = (input('Enter an integer: ')).upper()
   if not myNum: break
   
   print(myNum)
   oldNum = 0
   newNum = myNum
   
   while oldNum != newNum:
   	oldNum = newNum
   	newNum = calcSpecialNum(oldNum)
   	
   	print (newNum)