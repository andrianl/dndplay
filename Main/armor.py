class Armor:
    name = "Unknown Armor"
    cost = 0
    base_armor_class = 10
    dexterity_mod_max = None
    strength_required = None
    stealth_disadvantage = False
    weight = 0  # In lbs

    def __init__(self, name, cost=0, base_armor_class=10, dexterity_mod_max=None, strength_required=None,
                 stealth_disadvantage=False, weight=0):
        self.name = name
        self.cost = cost
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


#
# class LeatherArmor(LightArmor):
#     name = "Leather Armor"
#     cost = "10 gp"
#     base_armor_class = 11
#     weight = 10
#
#
# class HideArmor(MediumArmor):
#     name = "Hide Armor"
#     cost = "10 gp"
#     base_armor_class = 12
#     dexterity_mod_max = 2
#     weight = 12
#
#
# class ChainMail(HeavyArmor):
#     name = "Chain Mail"
#     cost = "75 gp"
#     base_armor_class = 16
#     dexterity_mod_max = 0
#     strength_required = 13
#     stealth_disadvantage = True
#     weight = 55


ChainMail = HeavyArmor(name='Chain Mail', cost=75, weight=55, base_armor_class=16)
