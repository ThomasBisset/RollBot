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

def deck(x):
    seed(time.time())
    loop = 0
    card = []
    output = []
    while loop < x:
        suit = randint(0,3)
        number = randint(1,13)
        if number == 1:
            card.append("Ace")
        elif number == 11:
            card.append("Jack")
        elif number == 12:
            card.append("Queen")
        elif number == 13:
            card.append("King")
        else: 
            card.append(str(number))
        if suit == 0:
            card.append("Spades")
        if suit == 1:
            card.append("Clubs")
        if suit == 2:
            card.append("Hearts")
        if suit == 3:
            card.append("Diamonds")
        output.append(card[0] + " of " + card[1])
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