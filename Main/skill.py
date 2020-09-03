from Main.stats import Ability, Strength, Dexterity, Intelligence, Wisdom, Charisma, Constitution


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

# print(Strength)
# print(Dexterity)
# print(Constitution)
# print(Intelligence)
# print(Wisdom)
# print(Charisma)
#
# print(acrobatics)
# print(nature)
# print(survival)
# print(perfomance)
