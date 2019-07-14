"""
    Author: KardasR

    To see results, find folder where this file is.
    Next, look for the file named"roll_visualized.svg".
    *Next, Drag that file and drop it into an internet browser.
    BAM! You can now see your results!

    * Or you can copy the path to the file.
    Then, paste it into a web browser and there you go!
"""

import pygal


def visualize(num_dice, sides, output, rolls):
    """This function will make a svg file to visualize your rolls."""

    # Setup for X axis
    y_list = []
    for i in range(1, sides + 1):
        y_list.append(i)

    # Visualize.
    hist = pygal.Bar()
    hist.title = "Results of dice roll"
    hist.x_labels = rolls
    hist.y_labels = y_list
    hist._y_title = "Rolls"
    hist.add('Rolls', rolls)
    hist.render_to_file('roll_visualized.svg')
