import Main.armor as armor
import Main.backgrounds  as backgrounds
import Main.classes as clses
import Main.dice as dice
import Main.race as race
import Main.stats as stat
import Main.weapon as weapon
import sys


class Character:
    Race = race.Race
    clss = clses.CharClass
    background = backgrounds.Background

    Strength = stat.Ability
    Dexterity = stat.Ability
    Constitution = stat.Ability
    Intelligence = stat.Ability
    Wisdom = stat.Ability
    Charisma = stat.Ability

    acrobatics = stat.Skill
    animal_handling = stat.Skill
    arcana = stat.Skill
    athletics = stat.Skill
    deception = stat.Skill
    history = stat.Skill
    insight = stat.Skill
    intimidation = stat.Skill
    investigation = stat.Skill
    medicine = stat.Skill
    nature = stat.Skill
    perception = stat.Skill
    perfomance = stat.Skill
    persuasion = stat.Skill
    religion = stat.Skill
    sleight_of_hand = stat.Skill
    stealth = stat.Skill
    survival = stat.Skill

    armor_class = stat.ArmorClass.ac

    speed = 30

    initiative = int

    max_health_point = int

    current_health = int

    hp_hit_dice = []

    level = 1

    def __init__(self, race, clss, background, level, armor_, weapon, abilities=[]):
        self.Race = race
        self.clss = clss
        self.background = background
        self.level = level

        self.max_health_point = dice.Dice.roll([self.level, clss.hit_die])
        self.armor_class = stat.ArmorClass(armor.ChainMail, armor.HeavyArmor).ac

        self.Strength = stat.Ability(abilities[0])
        self.Dexterity = stat.Ability(abilities[1])
        self.Constitution = stat.Ability(abilities[2])
        self.Intelligence = stat.Ability(abilities[3])
        self.Wisdom = stat.Ability(abilities[4])
        self.Charisma = stat.Ability(abilities[5])

        self.initiative = self.Dexterity.modifier
        self.speed = self.Race.speed

        self.acrobatics = stat.Skill('Acrobatics', self.Dexterity)
        self.animal_handling = stat.Skill('Animal_handling', self.Wisdom)
        self.arcana = stat.Skill('Arcana', self.Intelligence)
        self.athletics = stat.Skill('Athletics', self.Strength)
        self.deception = stat.Skill('Deception', self.Charisma)
        self.history = stat.Skill('History', self.Intelligence)
        self.insight = stat.Skill('Insight', self.Wisdom)
        self.intimidation = stat.Skill('Intimidation', self.Charisma)
        self.investigation = stat.Skill('Investigation', self.Intelligence)
        self.medicine = stat.Skill('Medicine', self.Wisdom)
        self.nature = stat.Skill('Nature', self.Intelligence)
        self.perception = stat.Skill('Perception', self.Wisdom)
        self.perfomance = stat.Skill('Perfomance', self.Charisma)
        self.persuasion = stat.Skill('Persuasion', self.Charisma)
        self.religion = stat.Skill('Religion', self.Intelligence)
        self.sleight_of_hand = stat.Skill('Sleight_of_hand', self.Dexterity)
        self.stealth = stat.Skill('Stealth', self.Dexterity)
        self.survival = stat.Skill('Survival', self.Wisdom)

    def __str__(self):
        return f"""
Race: {self.Race.name}
Class: {self.clss.name}
Background: {self.background.name}
Strength: {self.Strength.score}
Dexterity: {self.Dexterity.score} 
Constitution: {self.Constitution.score}
Intelligence: {self.Intelligence.score}
Wisdom: {self.Wisdom.score}
Charisma: {self.Charisma.score}
HP: {self.max_health_point}
Armour Class: {self.armor_class.ac}
Initiative: {self.initiative}
Speed: {self.speed}
"""


random_stats = [dice.Dice.random_stat_generator(), dice.Dice.random_stat_generator(), dice.Dice.random_stat_generator(),
                dice.Dice.random_stat_generator(), dice.Dice.random_stat_generator(), dice.Dice.random_stat_generator()]

Andy = Character(race.Dwarf, clses.Barbarian, backgrounds.Soldier, 1, armor.ChainMail, weapon.Handaxe, random_stats)
#
# print(Andy)
#
# print(sys.getsizeof(Andy))
