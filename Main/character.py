import Main.race as race
import Main.stats as stat
import Main.classes as clsses
import Main.background  as background
from Main.dice import Dice as dice
import Main.armor as armor


class Character:
    Race = race.Race
    clss  = clsses.CharClass
    background = background.Background

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

    armor_class = stat.ArmorClass

    speed = 30

    initiative = int

    max_health_point = int

    current_health = int

    hp_hit_dice = []

    level = 1

    # def __init__(self, abilities=[10, 10, 10, 10, 10, 10],
    #              level,
    #              race_instance,
    #              armor_instance,
    #              speed):
    #     self.Strength = abilities[0]
    #     self.Dexterity = abilities[1]
    #     self.Constitution = abilities[2]
    #     self.Intelligence = abilities[3]
    #     self.Wisdom = abilities[4]
    #     self.Charisma = abilities[5]
    #     self.level = level
    #     if isinstance(race_instance, race.Race):
    #         self.Race = race_instance
    #     if isinstance(armor_instance, armor.Armor):
    #         self.armor_class = armor_instance
    #     self.speed = speed
    #     pass

    def __init__(self, race, clss, background, level, armor_, weapon, abilities= []):
        self.Race = race
        self.clss = clss
        self.background = background
        self.level = level

        self.max_health_point = dice.roll([self.level, clss.hit_dice])
        self.armor_class = stat.ArmorClass(armor_, armor.Armor)

        self.Strength = stat.Ability('Strength', abilities[0])
        self.Dexterity = stat.Ability('Dexterity', abilities[1])
        self.Constitution = stat.Ability('Constitution', abilities[2])
        self.Intelligence = stat.Ability('Intelligence', abilities[3])
        self.Wisdom = stat.Ability('Wisdom', abilities[4])
        self.Charisma = stat.Ability('Charisma', abilities[5])

        self.initiative = self.Dexterity

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

        pass
