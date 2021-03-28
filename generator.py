# RollBot: a Python Script to play or enable the playing of a variety of simple games. Included are tools for dice rolling, coin flipping, playing rock-paper-scissors and Russian Roulette.
# Copyright (C) 2021 Thomas Bisset

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
