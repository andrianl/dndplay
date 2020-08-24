import random


class Dice:
    def __init__(self, dice: list):
        """

        :type dice: list
        """
        self.dice = dice

    def roll(self, dice):
        return random.randint(self.dice[0], self.dice[0]*self.dice[1])

    def random_stat_generator(self, numbers=1, dice=6):
        stat = [self.roll(numbers, dice), self.roll(numbers, dice), self.roll(numbers, dice), self.roll(numbers, dice)]
        stat.sort()
        return sum(stat) - stat[0]


_1d20 = Dice([1, 20])

print(_1d20.roll([1, 20]))

