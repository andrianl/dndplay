from collections import defaultdict

from Main import stats, dice, weapon, armor


class CharClass:
    """
    A generic Character Class (not to be confused with builtin class)
    """
    name = "Default"
    level = 1
    primary_abilities = stats.Ability
    hit_dice = dice.D10
    hp1lvl = 10 + stats.Constitution.modifier
    hpperlvl = [level, dice.D10] + level * stats.Constitution.modifier
    weapon_proficiencies = ()
    armor_proficiencies = ()
    tools = ()
    saving_throws = (stats.Ability, stats.Ability)
    languages = ()
    num_skill_choices = 2
    choose_skills = []
    skills_proficiency = ()
    start_equipment = ()
    spell_casting = False
    spellcasting_ability = stats.Ability
    cantrips = 0
    spells_slots_by_level = int
    spells_known = ()
    spells_prepared = ()
    subclass = False
    subclasses_available = ()
    features_by_level = defaultdict(list)
    description = """""" """"""


class Barbarian(CharClass):
    name = 'Barbarian'
    primary_abilities = stats.Strength
    level = 1
    hit_dice = [1, 12]
    hp1lvl = 12 + stats.Constitution.modifier
    hpperlvl = dice.Dice.roll([level, 12]) + level * stats.Constitution.modifier
    weapon_proficiencies = weapon.simple_weapons + weapon.martial_weapons
    armor_proficiencies = armor.light_armors + armor.medium_armors + armor.shields
    saving_throws = stats.Strength, stats.Constitution
    choose_skills = 2
    skills_proficiency = stats.animal_handling, stats.athletics, stats.intimidation, \
                         stats.nature, stats.perception, stats.survival
    start_equipment = ()
    description = '''
    A tall human tribesman strides through a blizzard, draped in fur and hefting his axe. He laughs as he charges toward the frost giant who dared poach his people’s elk herd.
A half-orc snarls at the latest challenger to her authority over their savage tribe, ready to break his neck with her bare hands as she did to the last six rivals.
Frothing at the mouth, a dwarf slams his helmet into the face of his drow foe, then turns to drive his armored elbow into the gut of another.
These barbarians, different as they might be, are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea.
For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength.
    '''


class Bard(CharClass):
    name = 'Bard'
    level = 1
    primary_abilities = stats.Charisma
    hit_dice = [1, 8]
    hp1lvl = 8 + stats.Constitution.modifier
    hpperlvl = [level, 8] + level * stats.Constitution.modifier
    weapon_proficiencies = weapon.simple_weapons
    tools = ()
    saving_throws = stats.Dexterity, stats.Charisma
    choose_skills = 3
    skills_proficiency = ()
    start_equipment = ()
    spell_casting = True
    spellcasting_ability = stats.Charisma
    cantrips = 2
    spells_slots_by_level = 2
    spells_known = 4
    description = '''
    Humming as she traces her fingers over an ancient monument in a long-forgotten ruin, a half-elf in rugged leathers finds knowledge springing into her mind, conjured forth by the magic of her song—knowledge of the people who constructed the monument and the mythic saga it depicts.
A stern human warrior bangs his sword rhythmically against his scale mail, setting the tempo for his war chant and exhorting his companions to bravery and heroism. The magic of his song fortifies and emboldens them.
Laughing as she tunes her cittern, a gnome weaves her subtle magic over the assembled nobles, ensuring that her companions’ words will be well received.
Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds.
    '''
