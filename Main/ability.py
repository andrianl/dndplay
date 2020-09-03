import math

from Main.dice import Dice
from constants.dices import D20


class Ability:
    name = ''
    modifier = 0

    def __init__(self, name, score=10):
        self.name = name
        self.score = score
        self.modifier = math.floor((self.score - 10) / 2)

    def __str__(self):
        return f'{self.name} : {self.score} : {self.modifier}'


Strength = Ability("Strength", Dice.roll([1, D20]))
Dexterity = Ability("Dexterity", Dice.roll([1, D20]))
Constitution = Ability("Constitution", Dice.roll([1, D20]))
Intelligence = Ability("Intelligence", Dice.roll([1, D20]))
Wisdom = Ability("Wisdom", Dice.roll([1, D20]))
Charisma = Ability("Charisma", Dice.roll([1, D20]))

# print(Strength)
# print(Dexterity)
# print(Constitution)
# print(Intelligence)
# print(Wisdom)
# print(Charisma)
