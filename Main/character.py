import Main.race as race
import Main.stats as stat
import Main.armor as armor


class Character:
    Race = race.Race

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

    def __init__(self, race, class_, background, level, armor, weapon):
        pass
