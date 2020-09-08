import random

D20 = 20
D4 = 4
D8 = 8
D12 = 12
D10 = 10
D100 = 100



class Dice:
    def __init__(self, dice):
        # self.number = number
        self.dice = dice

    @staticmethod
    def roll(dice):
        return random.randint(dice[0], dice[0] * dice[1])

    @staticmethod
    def roll_with_advantage(dice):
        return max(Dice.roll(dice), Dice.roll(dice))

    @staticmethod
    def roll_with_disadvantage(dice):
        return min(Dice.roll(dice), Dice.roll(dice))
