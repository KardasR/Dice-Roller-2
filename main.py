from roller import roll, show_rolls, rolls

"""Main file for Dice Roller 2."""

while True:
    sides = int(input("What sided dice would you like to roll? (Press 0 to exit)\n"))
    # Exit condition.
    if(sides == 0):
        break
    
    num_dice = int(input("How many dice would you like to roll?\n"))

    # Check for a critical.
    if(sides == 20 and num_dice == 1):
        output = roll(sides, num_dice)

        if(output == 20):
            print("Critical Success!")
        elif(output == 1):
            print("Critical Failure!")

        print(output)

    else:
        print(roll(sides, num_dice))

    show_die = input("Would you like to see your individual rolls? (y / n)\n")

    # Exit condition.
    if(show_die != "y"):
        break

    print(show_rolls(num_dice))

    # Empties the rolls list to avoid answers accumulating in the list.
    rolls.clear()
