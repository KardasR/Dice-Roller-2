"""
    Author: KardasR

    Main file for Dice Roller 2.
"""

from roller import roll, rolls, show_rolls
from visual import visualize

while True:
    sides = int(input("What sided dice would you like to roll? (Press 0 to exit)\n"))
    # Exit condition.
    if(sides == 0):
        break
    
    num_dice = int(input("How many dice would you like to roll?\n"))

    output = roll(sides, num_dice)

    # Check for a critical.
    if(sides == 20 and num_dice == 1):
        if(output == 20):
            print("Critical Success!")
        elif(output == 1):
            print("Critical Failure!")

        print(output)

    print(output)

    show_die = input("Would you like to see your individual rolls? (y / n)\n")

    # Exit condition.
    if(show_die != "y"):
        break

    print(show_rolls(num_dice))

    # Visualize the rolls.
    vis_rolls = input("Would you like to visualize your rolls? (y / n)\n")
    if(vis_rolls == 'y'):
        visualize(num_dice, sides, output, rolls)

    # Empties the rolls list to avoid answers accumulating in the list.
    rolls.clear()
