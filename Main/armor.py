class Armor:
    name = "Unknown Armor"
    cost = "0 gp"
    base_armor_class = 10
    dexterity_mod_max = None
    strength_required = None
    stealth_disadvantage = False
    weight = 0  # In lbs


class LightArmor(Armor):
    pass


class MediumArmor(Armor):
    dexterity_mod_max = 2
    pass


class HeavyArmor(Armor):
    dexterity_mod_max = None
    strength_required = 13
    stealth_disadvantage = True


class LeatherArmor(LightArmor):
    name = "Leather Armor"
    cost = "10 gp"
    base_armor_class = 11
    weight = 10


class HideArmor(MediumArmor):
    name = "Hide Armor"
    cost = "10 gp"
    base_armor_class = 12
    dexterity_mod_max = 2
    weight = 12


class ChainMail(HeavyArmor):
    name = "Chain Mail"
    cost = "75 gp"
    base_armor_class = 16
    dexterity_mod_max = 0
    strength_required = 13
    stealth_disadvantage = True
    weight = 55
