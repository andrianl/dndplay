import sys

from PyQt5 import QtWidgets

import Main.character as char
import Main.dice as dice
import Main.weapon as weapon
from UI.character_sheet import Ui_CharacterSheet

# Create app
app = QtWidgets.QApplication(sys.argv)
# init
CharacterSheet = QtWidgets.QMainWindow()
ui = Ui_CharacterSheet()
ui.setupUi(CharacterSheet)
CharacterSheet.show()

# Logic

ui.cls_lbl.setText(f'Class: {char.char.clss.name}')
ui.race_lbl.setText(f'Race: {char.char.Race.name}')
ui.background_lbl.setText(f'Background: {char.char.background.name}')

ui.initiative.setText(f'Initiative: {char.char.initiative}')
ui.hp.setText(f'HP: {char.char.max_health_point}')
ui.speed.setText(f'Speed: {char.char.speed}')
ui.armor_class.setText(f'Armor Class: {char.char.armor_class}')

ui.strength_button.setText(
    f'Strength: {char.char.Strength.score}\nModificator: {char.char.Strength.modifier}')
ui.dexterity_button.setText(
    f'Dexterity: {char.char.Dexterity.score}\nModificator: {char.char.Dexterity.modifier}')
ui.constituion_button.setText(
    f'Constitution: {char.char.Constitution.score}\nModificator: {char.char.Constitution.modifier}')
ui.intelligence_button.setText(
    f'Intelligence: {char.char.Intelligence.score}\nModificator: {char.char.Intelligence.modifier}')
ui.wisdom_button.setText(f'Wisdom: {char.char.Wisdom.score}\nModificator: {char.char.Wisdom.modifier}')
ui.charisma_button.setText(
    f'Charisma: {char.char.Charisma.score}\nModificator: {char.char.Charisma.modifier}')


def strength_roll():
    modifier = char.char.Strength.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Strength = {d20} + {modifier} = {d20 + modifier}')


def dexterity_roll():
    modifier = char.char.Dexterity.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Dexterity = {d20} + {modifier} = {d20 + modifier}')


def constitution_roll():
    modifier = char.char.Constitution.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Constitution = {d20} + {modifier} = {d20 + modifier}')


def intelligence_roll():
    modifier = char.char.Intelligence.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Intelligence = {d20} + {modifier} = {d20 + modifier}')


def wisdom_roll():
    modifier = char.char.Wisdom.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Wisdom = {d20} + {modifier} = {d20 + modifier}')


def charisma_roll():
    modifier = char.char.Charisma.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Charisma = {d20} + {modifier} = {d20 + modifier}')


ui.strength_button.clicked.connect(strength_roll)
ui.dexterity_button.clicked.connect(dexterity_roll)
ui.constituion_button.clicked.connect(constitution_roll)
ui.intelligence_button.clicked.connect(intelligence_roll)
ui.wisdom_button.clicked.connect(wisdom_roll)
ui.charisma_button.clicked.connect(charisma_roll)

ui.weapon_name.setText(f'{char.char.weapons[0].name}')
ui.attack_btn.setText(f'Attack Bonus\n{char.char.Strength.modifier + char.char.proficiency_bonus}')
ui.damage_btn.setText(f'Damage/Type\n{char.char.weapons[0].base_damage[0]}'
                      f'd{char.char.weapons[0].base_damage[1]} + {char.char.Strength.modifier} '
                      f'/ {char.char.weapons[0].damage_type}')


def attack_():
    d20 = dice.Dice.roll([1, 20])
    attack_bonus = char.char.Strength.modifier + char.char.proficiency_bonus
    ui.dice_result.setText(f'D20 + Attack bonus = {d20} + {attack_bonus} = {d20 + attack_bonus}')
    if d20 == 20:
        ui.dice_result.setText(f'D20 + Attack bonus = {d20} + {attack_bonus} = {d20 + attack_bonus} Critical attack')


def damage_():
    d20 = dice.Dice.roll([1, 20])
    damage = dice.Dice.roll([char.char.weapons[0].base_damage[0], char.char.weapons[0].base_damage[1]])
    modifier = char.char.Strength.modifier
    ui.dice_result.setText(f'Damage: {damage} + {modifier} = {damage+modifier}')


ui.attack_btn.clicked.connect(attack_)
ui.damage_btn.clicked.connect(damage_)

# Main loop
sys.exit(app.exec_())
