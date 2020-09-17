from collections import defaultdict

import Main.armor as armor
import Main.stats
import Main.stats as stat
import Main.weapon as weapons
import constants.dices as dice


class CharClass:
    """
    A generic Character Class (not to be confused with builtin class)
    """
    name = "Default"
    level = 1
    hit_die = dice.D10
    primary_abilities = Main.stats.Ability
    weapon_proficiencies = ()
    armor_proficiencies = ()
    proficiencies_text = ''
    saving_throw_proficiencies = (Main.stats.Ability, Main.stats.Ability)
    languages = ()
    num_skill_choices = 2
    choose_skills = []
    skills_proficiency = ()
    start_equipment = ()
    spell_casting = False
    spellcasting_ability = Main.stats.Ability
    spell_slots_by_level = int
    spells_known = ()
    spells_prepared = ()
    subclass = False
    subclasses_available = ()
    features_by_level = defaultdict(list)
    description = """""" """"""


class Barbarian(CharClass):
    name = 'Barbarian'
    hit_die = dice.D12
    primary_abilities = stat.Strength
    weapon_proficiencies = weapons.martial_weapons & weapons.simple_weapons
    armor_proficiencies = (armor.LightArmor, armor.MediumArmor)
    saving_throw_proficiencies = (stat.Strength, stat.Constitution)
    choose_skills = [stat.animal_handling, stat.athletics, stat.intimidation,
                     stat.nature, stat.perception, stat.survival]
