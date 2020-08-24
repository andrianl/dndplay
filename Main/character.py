import math


class Character:
    def __init__(self, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma):
        self.Strength = Strength
        self.Dexterity = Dexterity
        self.Constitution = Constitution
        self.Intelligence = Intelligence
        self.Wisdom = Wisdom
        self.Charisma = Charisma

    @staticmethod
    def stat_modificator(stat):
        return math.floor((stat - 10) / 2)
