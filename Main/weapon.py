import Main.stats as stat
import Main.wage as coin


class Ammunition:
    name = 'name'
    numbers = 20

    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers


class Weapon:
    name = "Weapon"
    cost = coin.Coin.cost
    base_damage = [1, 4]  # 1d4
    ability = stat.Ability.modifier
    simple = False
    martial = False
    ammunition = Ammunition
    finesse = False
    damage_type = ""
    heavy = False
    light = False
    loading = 0
    range = 20
    long_range = 60
    reach = 5
    two_handed = False
    thrown = False
    versatile = False

    def __init__(self, name, cost=coin.Coin, damage=None, ability=stat.Strength, simple=False, martial=False,
                 ammunition=None,
                 finesse=False,
                 damage_type='slashing', heavy=False, light=False, loading=0, range_=20, long_range=60,
                 reach=5, two_handed=False, thrown=False, versatile=False):
        if damage is None:
            damage = [1, 4]
        self.name = name
        if isinstance(cost, coin.Coin):
            self.cost = cost.cost
        self.base_damage = damage
        if isinstance(ability, stat.Ability):
            self.ability = ability
        else:
            self.ability = stat.Strength
        self.simple = simple
        self.martial = martial
        self.ammunition = ammunition
        self.finesse = finesse
        self.damage_type = damage_type
        self.heavy = heavy
        self.light = light
        self.loading = loading
        self.range = range_
        self.long_range = long_range
        self.reach = reach
        self.two_handed = two_handed
        self.thrown = thrown
        self.versatile = versatile


class ImprovisedWeapon(Weapon):
    base_damage = [1, 4]
    range = 20
    long_range = 60


class SilveredWeapon(Weapon):
    pass


class SpecialWeapon(Weapon):
    pass
