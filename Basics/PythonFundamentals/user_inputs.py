value = input("Please enter a value:\n")






print(value)

import sys
import random

print("")
playerchoice = input("Enter ... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")
player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("You myst enter 1, 2, or 3")
    
computerchoice = random.choice("123")
computer = int(computerchoice)