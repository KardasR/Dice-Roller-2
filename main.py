from roller import roll, show_rolls

"""Main file for Dice Roller 2."""

while True:
    sides = int(input("What sided dice would you like to roll? (Press 0 to exit)\n"))
    if(sides == 0):
        break
    
    num_dice = int(input("How many dice would you like to roll?\n"))

    print(roll(sides, num_dice))

    show_die = input("Would you like to see your individual rolls? (y / n)\n")

    if(show_die != "y"):
        break

    rolls = show_rolls(num_dice)

    print(rolls)
