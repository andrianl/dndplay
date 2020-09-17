from Main.dice import Dice
import Main.stats as stat
import Main.character as ch


class Weapon:
    name = "Weapon"
    cost = 0
    base_damage = [1, 4]  # 1d4
    damage_bonus = 0
    attack_bonus = 2
    damage_type = ""
    weight = 1  # In lbs
    properties = ""
    ability = stat.Ability.modifier
    is_finesse = False
    features_applied = False

    def __init__(self, name, cost=0, base_damage=[1, 4], damage_bonus=0, attack_bonus=2, damage_type="",
                 weight=1, properties="", ability_=0, is_finesse=False, features_applied=False):
        self.name = name
        self.cost = cost
        self.base_damage = base_damage
        self.damage_bonus = damage_bonus
        self.attack_bonus = attack_bonus
        self.damage_type = damage_type
        self.weight = weight
        self.properties = properties
        if isinstance(ability_, stat.Ability):
            self.ability = ability_.modifier

        self.is_finesse = is_finesse
        self.features_applied = features_applied

    def attack(self, base_damage):
        return Dice.roll(self.base_damage) + self.ability + self.attack_bonus

    def damage(self, base_damage):
        return Dice.roll(self.base_damage) + self.ability


class MeleeWeapon(Weapon):
    name = "Melee Weapons"
    ability = stat.Strength.modifier


class RangedWeapon(Weapon):
    name = "Ranged Weapons"
    ability = stat.Dexterity.modifier


# class SimpleWeapon(Weapon):
#     name = "Simple Weapons"
#
#
# class MartialWeapon(Weapon):
#     name = "Martial Weapons"
martial_weapons = set()
simple_weapons = set()

BattleAxe = MeleeWeapon(name='Battle Axe', base_damage=[1, 8], damage_type='slashing',
                        properties='versatile', weight=4)

# # # Some lists of weapons for easy proficiency resolution
# # simple_melee_weapons = {Club, Dagger, Greatclub, Handaxe, Javelin, LightHammer, Mace, Quarterstaff, Sickle, Spear}
# # simple_ranged_weapons = {LightCrossbow, Dart, Shortbow, Sling}
# # simple_weapons = simple_melee_weapons & simple_ranged_weapons
# #
# # martial_melee_weapons = {Battleaxe, Flail, Glaive, Greataxe, Greatsword, Halberd, Lance, Longsword, Maul, Morningstar,
# #                          Pike, Rapier, Scimitar, Shortsword, ThrowingHammer, Trident, WarPick, Warhammer, Whip}
# # martial_ranged_weapons = {Blowgun, HandCrossbow, HeavyCrossbow, Longbow, Net}
# # martial_weapons = martial_melee_weapons & martial_ranged_weapons
# #
# # monk_weapons = {Shortsword, Unarmed, Club, Dagger, Handaxe, Javelin, LightHammer, Mace, Quarterstaff, Sickle, Spear,
# #                 SunBolt}
# #
# # # firearms = Set[Firearm, Blunderbuss, Pistol, Musket]
