from collections import defaultdict

import Main
from Features import races
from Main import weapon


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


class Dwarf(Race):
    name = "Dwarf"
    size = "medium"
    speed = 25
    languages = {"Common", "Dwarvish"}
    constitution_bonus = 2
    proficiencies_text = ('battleaxes', 'handaxes', 'throwing hammers',
                          'warhammers')
    weapon_proficiences = {weapon.Battleaxe, Main.weapon.Handaxe,
                           Main.weapon.ThrowingHammer, Main.weapon.Warhammer}
    features = {races.Darkvision, races.DwarvenResilience, races.Stonecunning}


class HillDwarf(Dwarf):
    name = "Hill Dwarf"
    wisdom_bonus = 1
    hit_point_bonus = 1
    features = Dwarf.features & {races.DwarvenToughness}


class MountainDwarf(Dwarf):
    name = "Mountain Dwarf"
    strength_bonus = 2


# Elves
class Elf(Race):
    name = "Elf"
    size = "medium"
    speed = 30
    dexterity_bonus = 2
    skill_proficiencies = {'perception'}
    languages = ('Common', 'Elvish')
    features = {races.Darkvision, races.FeyAncestry, races.Trance}


class HighElf(Elf):
    name = "High Elf"
    weapon_proficiencies = {weapon.Longsword, weapon.Shortsword,
                            weapon.Shortbow, weapon.Longbow}
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')
    intelligence_bonus = 1
    languages = ('Common', 'Elvish', '[choose one]')
    features = Elf.features & {races.ElfCantrip}


class WoodElf(Elf):
    name = "Wood Elf"
    weapon_proficiencies = {weapon.Longsword, weapon.Shortsword,
                            weapon.Shortbow, weapon.Longbow}
    proficiencies_text = ('longswords', 'shortswords', 'shortbows', 'longbows')
    wisdom_bonus = 1
    speed = 35
    features = Elf.features & {races.MaskOfTheWild}


class DarkElf(Elf):
    name = "Dark Elf"
    weapon_proficiencies = (weapon.Rapier, weapon.Shortsword,
                            weapon.HandCrossbow)
    proficiencies_text = ('rapiers', 'shortswords', 'hand crossbows')
    charisma_bonus = 1
    features = Elf.features & {races.SuperiorDarkvision,
                               races.SunlightSensitivity}
    # spells_known = (spells.DancingLights,)


# Halflings
class Halfling(Race):
    name = "Halfling"
    size = "small"
    speed = 25
    dexterity_bonus = 2
    languages = ('Common', 'Halfling')
    features = {races.Lucky, races.Brave, races.HalflingNimbleness}


class LightfootHalfling(Halfling):
    name = "Lightfoot Halfling"
    charisma_bonus = 1
    features = Halfling.features & {races.NaturallyStealthy}


class StoutHalfling(Halfling):
    name = "Stout Halfling"
    constitution_bonus = 1
    features = Halfling.features & {races.StoutResilience}


# Humans
class Human(Race):
    name = "Human"
    size = "medium"
    speed = 30
    strength_bonus = 1
    dexterity_bonus = 1
    constitution_bonus = 1
    intelligence_bonus = 1
    wisdom_bonus = 1
    charisma_bonus = 1
    languages = ("Common", '[choose one]')


# Dragonborn
class Dragonborn(Race):
    name = "Dragonborn"
    size = "medium"
    speed = 30
    strength_bonus = 2
    charisma_bonus = 1
    languages = ("Common", "Draconic")
    features = (races.DraconicAncestry, races.BreathWeapon,
                races.DraconicResistance)


# Gnomes
class _Gnome(Race):
    name = "Gnome"
    size = "small"
    speed = 25
    intelligence_bonus = 2
    languages = ("Common", "Gnomish")
    features = {races.Darkvision, races.GnomeCunning}


class ForestGnome(_Gnome):
    name = "Forest Gnome"
    dexterity_bonus = 1
    features = _Gnome.features & {races.NaturalIllusionist,
                                  races.SpeakWithSmallBeasts}
    # spells_known = (spells.MinorIllusion,)


class RockGnome(_Gnome):
    name = "Rock Gnome"
    constitution_bonus = 1
    features = _Gnome.features & {races.ArtificersLore,
                                  races.Tinker}


class DeepGnome(_Gnome):
    name = "Deep Gnome"
    dexterity_bonus = 1
    languages = ("Common", "Gnomish", "Undercommon")
    features = _Gnome.features & {races.SuperiorDarkvision, races.StoneCamouflage}


# Half-elves
class HalfElf(Race):
    name = "Half-Elf"
    size = "medium"
    speed = 30
    charisma_bonus = 2
    skill_choices = ('acrobatics', 'animal handling', 'arcana',
                     'athletics', 'deception', 'history', 'insight',
                     'intimidation', 'investigation', 'medicine', 'nature',
                     'perception', 'performance', 'persuasion', 'religion',
                     'sleight of hand', 'stealth', 'survival')
    num_skill_choices = 2
    languages = ("Common", "Elvish", "[choose one]")
    features = {races.Darkvision, races.FeyAncestry}


# Half-Orcs
class HalfOrc(Race):
    name = "Half-Orc"
    size = "medium"
    speed = 30
    strength_bonus = 2
    constitution_bonus = 1
    skill_proficiencies = ('intimidation',)
    languages = ("Common", "Orc")
    features = {races.Darkvision, races.RelentlessEndurance,
                races.SavageAttacks}


# Tielflings
class Tiefling(Race):
    name = "Tiefling"
    size = "medium"
    speed = 30
    intelligence_bonus = 1
    charisma_bonus = 2
    languages = ("Common", "Infernal")
    features = {races.Darkvision, races.HellishResistance}  # plus infernal legacy
