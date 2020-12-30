import random
import time
import sys

class Dice:
    """ Purpose   : Serve as an API for DICE Simulator.
        min (int) : minimum random number in dice roll
        max (int) : amaximum random number in dice roll"""
    def __init__(self,
                 min=1,
                 max=6):
        try:
            min=int(min)
            max=int(max)
        except:
            min=1
            max=6

        self.min = min
        self.max = max

    def roll(self):
        """ Returns a random integer between the minimum and maximum values
            given at initialization. """
        self.current_roll = random.randint(self.min, self.max)
        return self.current_roll

    def walk(self):
        self.roll()

        if self.current_roll == 6:
            print("    -------")
            print("  |         |")
            print(" |  *     *  |")
            print("|   *     *   |")
            print(" |  *     *  |")
            print("  |         |")
            print("    -------")
            print('"So The Dice Walk Helped I See"')
        else:
            print("\nNo Luck, You Need To Go For a Dice Walk Man")

    def roll_console(self):
        print("\nRolling Dice . . .")
        self.roll()

        if self.current_roll == 1:
            print("    -------")
            print("  |         |")
            print(" |           |")
            print("|      *      |")
            print(" |           |")
            print("  |         |")
            print("    -------")
        if self.current_roll == 2:
            print("    -------")
            print("  |         |")
            print(" |        *  |")
            print("|             |")
            print(" |  *        |")
            print("  |         |")
            print("    -------")
        if self.current_roll == 3:
            print("    -------")
            print("  |         |")
            print(" |     *     |")
            print("|             |")
            print(" |  *     *  |")
            print("  |         |")
            print("    -------")
        if self.current_roll == 4:
            print("    -------")
            print("  |         |")
            print(" |   *   *   |")
            print("|             |")
            print(" |   *   *   |")
            print("  |         |")
            print("    -------")
        if self.current_roll == 5:
            print("    -------")
            print("  |         |")
            print(" |  *     *  |")
            print("|      *      |")
            print(" |  *     *  |")
            print("  |         |")
            print("    -------")
        if self.current_roll == 6:
            print("    -------")
            print("  |         |")
            print(" |  *     *  |")
            print("|   *     *   |")
            print(" |  *     *  |")
            print("  |         |")
            print("    -------")


        print("Roll Received: ", self.current_roll)
        return self.current_roll

if __name__ == "__main__":

    if len(sys.argv) == 2:
        dice = Dice(max=sys.argv[1])

        if sys.argv[1] == "walk":
            dice.walk()
        else:
            print(dice.roll())


    elif len(sys.argv) == 3:
        dice = Dice(min=sys.argv[1],max=sys.argv[2])
        print(dice.roll())

    else:
        dice = Dice()
        dice.roll_console()