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