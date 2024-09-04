import sys

pip  = "A47TK369Q258J"
suit = "CHSDCHSDCHSDCHSDC"

def rotate(l,n):
   return l[n:] + l[:n]

deck = [x+y for x,y in zip(pip,suit)]
deck2 = [x+y for x,y in zip(pip,rotate(suit,1))]
deck3 = [x+y for x,y in zip(pip,rotate(suit,2))]
deck4 = [x+y for x,y in zip(pip,rotate(suit,3))]

fullDeck = deck + deck2 + deck3 + deck4

while(True):
   #n = int(input('Enter cut number: '))
   #if n == 99: break

   #print 'Enter Bottom Card: '
   #bottomCard = sys.stdin.readline()
   bottomCard = (input('Enter Bottom Card: ')).upper()
   if not bottomCard: break

   print (bottomCard)
   print (fullDeck.index(bottomCard) + 1)
   n =  fullDeck.index(bottomCard) + 1

   fullDeck = rotate(fullDeck,n)
   print (fullDeck)

   card = (input('Enter a Card: ')).upper()

   print (card)
   print (fullDeck.index(card) + 1)