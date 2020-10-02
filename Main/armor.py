import Main.wage as coin


class Armor:
    name = "Unknown Armor"
    cost = coin.Coin.cost
    base_armor_class = 10
    dexterity_mod_max = None
    strength_required = None
    stealth_disadvantage = False
    weight = 0  # In lbs

    def __init__(self, name, cost=None, base_armor_class=10, dexterity_mod_max=None, strength_required=None,
                 stealth_disadvantage=False, weight=0):
        self.name = name
        if isinstance(cost, coin.Coin):
            self.cost = cost.point.cost
        self.base_armor_class = base_armor_class
        self.dexterity_mod_max = dexterity_mod_max
        self.strength_required = strength_required
        self.stealth_disadvantage = stealth_disadvantage
        self.weight = weight


class LightArmor(Armor):
    pass


class MediumArmor(Armor):
    dexterity_mod_max = 2
    pass


class HeavyArmor(Armor):
    dexterity_mod_max = None
    strength_required = 13
    stealth_disadvantage = True


class Shield(Armor):
    base_armor_class = 2


light_armors = ()
medium_armors = ()
heavy_armors = ()
shields = ()
