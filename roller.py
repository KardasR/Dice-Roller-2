"""
    Author: KardasR
"""

import random

rolls = []
def roll(sides, num_dice):
    """A function to roll the dice."""

    total = 0
    for i in range(num_dice):
        roll = random.randint(1,sides)        
        rolls.append(roll)
        total = total + roll

    return total

def show_rolls(num_dice):
    """A function to show individual rolls."""
    return(rolls)
