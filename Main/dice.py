import random


class Dice:
    def __init__(self, dice):
        # self.number = number
        self.dice = dice

    @staticmethod
    def roll(dice):
        return random.randint(dice[0], dice[0] * dice[1])

    # def random_stat_generator(self, numbers=1, dice=6):
    #     stat = [self.roll(numbers, dice), self.roll(numbers, dice), self.roll(numbers, dice), self.roll(numbers, dice)]
    #     stat.sort()
    #     return sum(stat) - stat[0]
    #


