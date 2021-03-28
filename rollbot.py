# RollBot: a Python Script to play or enable the playing of a variety of simple games. Included are tools for dice rolling, coin flipping, playing rock-paper-scissors and Russian Roulette.
# Copyright (C) 2021 Thomas Bisset

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import importlib
from generator import roll, flip, rps, rr

parser = argparse.ArgumentParser(description="RollBot | by Thomas Bisset")
parser.add_argument("action", type=str, choices=["roll", "flip", "rps", "rr"], default="roll", help="Tells the bot whether to roll some die, flip some coins, play Rock-Paper-Scissors or Russian Roulette!")
parser.add_argument("-d", type=int, default=20, help="Set how many sides the dice will have")
parser.add_argument("-x", type=int, default=1, help="Set how many times the action completes")

args = parser.parse_args()

if args.action == "roll":
    print(roll(args.d, args.x))
elif args.action == "flip":
    print(flip(args.x))
elif args.action == "rps":
    print(rps(args.x))
elif args.action =="rr":
    print(rr(args.x))