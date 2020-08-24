from collections import defaultdict


class Race:
    name = ''
    speed = 30
    size = 'medium'
    languages = ('Common',)
    proficiencies_text = tuple()
    weapon_proficiences = tuple()
    skill_proficiencies = ()
    skill_choices = ()
    num_skill_choices = 0
    features = tuple()
    features_by_level = defaultdict(list)
    strength_bonus = 0
    dexterity_bonus = 0
    constitution_bonus = 0
    intelligence_bonus = 0
    wisdom_bonus = 0
    charisma_bonus = 0
    hit_point_bonus = 0
    spells_known = ()

