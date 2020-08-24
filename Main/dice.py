import random


class Dice:
    def __init__(self, number, dice):
        self.number = number
        self.dice = dice

    def roll(self, number, dice):
        return random.randint(number, number * dice)

    def random_stat_generator(self, numbers=1, dice=6):
        stat = [self.roll(numbers, dice), self.roll(numbers, dice), self.roll(numbers, dice), self.roll(numbers, dice)]
        stat.sort()
        return sum(stat) - stat[0]
