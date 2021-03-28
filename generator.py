from random import randint
from random import seed
import time

def roll(d,x): 
 seed(time.time()) 
 loop = 0
 output = []
 while loop < x:
  result = randint(1, d)
  output.append(result)
  loop +=1
 return output

def flip(x):
 seed(time.time())
 loop = 0
 output = []
 while loop < x:
  result = randint(0,1)
  if result == 0:
   output.append("Heads")
  if result == 1: 
   output.append("Tails")
  loop +=1
 return output

def rps(x):
 seed(time.time())
 loop = 0
 output = []
 while loop < x:
  result = randint(0,2)
  if result == 0:
   output.append("Rock")
  if result == 1: 
   output.append("Paper")
  if result == 2:
   output.append("Scissors")
  loop +=1
 return output

def rr(x):
 seed(time.time())
 loop = 0
 output = []
 while loop < x:
  chamber = randint(0,5)
  bullet = randint(0,5)
  if bullet == chamber:
   output.append("* BANG! *")
  else:
   output.append("* click *")
  loop +=1
 return output
