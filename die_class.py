from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self,num_side=8):
        """Assume a 8-sided die"""
        self.num_side = num_side

    def roll_dice(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_side)
