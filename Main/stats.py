import math

from Main.armor import LightArmor, MediumArmor, HeavyArmor
from Main.dice import Dice
from constants.dices import D20


class Ability:
    score = 10
    modifier = 0

    def __init__(self, score=10):
        self.score = score
        self.modifier = math.floor((self.score - 10) / 2)

    def __get__(self, instance, ability):
        if isinstance(instance, Ability):
            return self.score

    def __add__(self, other):
        return other+self.modifier

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


class Skill:
    name = str
    modifier = 0

    def __init__(self, name, instance):
        self.name = name
        if isinstance(instance, Ability):
            self.modifier = instance.modifier
        else:
            self.modifier = 10

    def __str__(self):
        return f'{self.name} : {self.modifier}'

    def __get__(self, instance, skill):
        if isinstance(instance, Skill):
            return self.modifier


class ArmorClass:
    ac = 0

    def __init__(self, instance, armor):
        self.instance = instance
        self.armor = armor
        if isinstance(instance, LightArmor):
            self.ac = instance.base_armor_class + Dexterity
        elif isinstance(instance, MediumArmor):
            self.ac = instance.base_armor_class + min(instance.dexterity_mod_max, Dexterity)
        elif isinstance(instance, HeavyArmor):
            self.ac = instance.base_armor_class

    # def __get__(self, instance, armor):
    #     if isinstance(instance, LightArmor):
    #         self.ac = instance.base_armor_class + Dexterity
    #     elif isinstance(instance, MediumArmor):
    #         self.ac = instance.base_armor_class + min(instance.dexterity_mod_max, Dexterity)
    #     elif isinstance(instance, HeavyArmor):
    #         self.ac = instance.base_armor_class
    #
    #     return self.ac


Strength = Ability(Dice.roll([1, D20]))
Dexterity = Ability(Dice.roll([1, D20]))
Constitution = Ability( Dice.roll([1, D20]))
Intelligence = Ability(Dice.roll([1, D20]))
Wisdom = Ability( Dice.roll([1, D20]))
Charisma = Ability(Dice.roll([1, D20]))

acrobatics = Skill('Acrobatics', Dexterity)
animal_handling = Skill('Animal_handling', Wisdom)
arcana = Skill('Arcana', Intelligence)
athletics = Skill('Athletics', Strength)
deception = Skill('Deception', Charisma)
history = Skill('History', Intelligence)
insight = Skill('Insight', Wisdom)
intimidation = Skill('Intimidation', Charisma)
investigation = Skill('Investigation', Intelligence)
medicine = Skill('Medicine', Wisdom)
nature = Skill('Nature', Intelligence)
perception = Skill('Perception', Wisdom)
perfomance = Skill('Perfomance', Charisma)
persuasion = Skill('Persuasion', Charisma)
religion = Skill('Religion', Intelligence)
sleight_of_hand = Skill('Sleight_of_hand', Dexterity)
stealth = Skill('Stealth', Dexterity)
survival = Skill('Survival', Wisdom)
