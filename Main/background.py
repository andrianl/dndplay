import Main.stats as skill


class Background():
    name = "Generic background"
    skill_proficiencies = ()
    weapon_proficiencies = ()
    armor_proficiencies = ()
    tool_proficiencies = ()
    proficiencies_text = ()
    skill_choices = ()
    num_skill_choices = 0
    features = ()
    languages = ()
    speciality = ()
    start_equipment = ()


class CustomBackgroung(Background):
    def __init__(self, name,
                 skill_proficiencies,
                 weapon_proficiencies,
                 armor_proficiencies,
                 skill_choices,
                 num_skill_choices,
                 features,
                 languages):
        self.name = name
        self.skill_proficiencies = skill_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.skill_choices = skill_choices
        self.num_skill_choices = num_skill_choices
        self.features = features
        self.languages = languages


class Soldier(Background):
    name = 'Soldier'
    skill_proficiencies = [skill.athletics, skill.intimidation]
