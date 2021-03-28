# RollBot

**RollBot** is a Python Script to play or enable the playing of a variety of simple games. Included are tools for dice rolling, coin flipping, playing rock-paper-scissors and of course everyone's favorite parlour game, Russian Roulette.

Originally I intended this to work as a Discord bot and while I had it working (hosted on a Raspberry Pi) I ended up doing something which broke it again, and for the life of me I can't work out what it is I did wrong! I plan on improving functionality before looking to deploy it again.

## Usage

**RollBot** requires one of four arguments: `roll`, `flip`, `rps` or `rr`.

Underneath, the script is essentially a random-number generator. The above arguments alter how the random number is interpreted and outputted to screen. 

`roll` is unique among the tools as this will take an additional argument (`-d`) which allows you to set how many sides the dice has. By default (no arguements), `roll` assumes a D20 is being used: 

    $ python3 rollbot.py roll
    [14]    

For a six-sided die you would run: 

    $ python3 rollbot.py roll -d 6
    [4]

> Note that `-d` is not restricted to "normal" die - as long as the number is an integer it will generate a random number between `1` and `d`. For example, you could roll a thirteen-sided die if you wanted:

    $ python3 rollbot.py roll -d 13
    [13]

`flip` and `rps` should be pretty straightforward, outputting either "Heads" or "Tails" (for the former) and "Rock", "Paper" or "Scissors" (for the latter).

    $ python3 rollbot.py flip
    ['Tails']
    $ python3 rollbot.py rps
    ['Scissors']

`rr` works by picking two random integers between 1 and 6 and puts each into variables `bullet` and `chamber`. The two variables are then compared; if they match, the bullet is fired and you are "dead" - if they do not match, then you are "alive".

    $ python3 rollbot.py rr
    ['* click *']

The `-x` argument can be used to do multiple rolls at once. For example, if you are playing *Dungeons & Dragons* and your DM requires you to roll four D4's for damage, you can run:

    $ python3 rollboy.py roll -x 4 -d 4
    [3, 1, 3, 2]

At the moment this works for `roll`, `flip` and `rps` but does not work for Russian Roulette as intended. For example:

    $ python3 rollbot.py rr -x 6
    ['* click *', '* BANG! *', '* click *', '* click *', '* BANG! *', '* click *']

I plan on correcting this behaviour so that "follow-up games" work as they might in the real world (except with less lethality, obviously!)

`-h` displays these commands as well, should you ever need it.

## Files

`generator.py` could be considered the "back-end". It is made up of the various functions of the script and essentially does most of the work. 

`rollbot.py` is the "front-end" CLI, and is fairly uncomplicated. At the moment this file exists purely for the sake of testing the script. 

`readme.md` is the file you are reading right now. `license.md` is the license file (GPL v3).