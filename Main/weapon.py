from Main.dice import Dice


class Weapon():
    name = ""
    cost = "0 gp"
    base_damage = [1, 4]  # 1d4
    damage_bonus = 0
    attack_bonus = 0
    damage_type = "p"
    weight = 1  # In lbs
    properties = ""
    ability = 'strength'
    is_finesse = False
    features_applied = False

    @staticmethod
    def damage(base_damage):
        return Dice.roll(base_damage)


sword = Weapon()


