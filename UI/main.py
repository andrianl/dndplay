import sys
from PySide2 import QtWidgets
from PyQt5 import QtCore, QtWidgets
from PySide2.QtCore import QRect, QMetaObject
from PySide2.QtWidgets import QWidget, QFrame, QPushButton, QLabel, QMenuBar, QMenu, QStatusBar
from UI.character_sheet import Ui_CharacterSheet
import Main.character as char
import Main.dice as dice

# Create app
app = QtWidgets.QApplication(sys.argv)
# init
CharacterSheet = QtWidgets.QMainWindow()
ui = Ui_CharacterSheet()
ui.setupUi(CharacterSheet)
CharacterSheet.show()


# Logic

ui.cls_lbl.setText(f'Class: {char.character.clss.name}')
ui.race_lbl.setText(f'Race: {char.character.Race.name}')
ui.background_lbl.setText(f'Background: {char.character.background.name}')



ui.initiative.setText(f'Initiative: {char.character.initiative}')
ui.hp.setText(f'HP: {char.character.max_health_point}')
ui.speed.setText(f'Speed: {char.character.speed}')
ui.armor_class.setText(f'Armor Class: {char.character.armor_class}')



ui.strength_button.setText(f'Strength: {char.character.Strength.score}\nModificator: {char.character.Strength.modifier}')
ui.dexterity_button.setText(f'Dexterity: {char.character.Dexterity.score}\nModificator: {char.character.Dexterity.modifier}')
ui.constituion_button.setText(f'Constitution: {char.character.Constitution.score}\nModificator: {char.character.Constitution.modifier}')
ui.intelligence_button.setText(f'Intelligence: {char.character.Intelligence.score}\nModificator: {char.character.Intelligence.modifier}')
ui.wisdom_button.setText(f'Wisdom: {char.character.Wisdom.score}\nModificator: {char.character.Wisdom.modifier}')
ui.charisma_button.setText(f'Charisma: {char.character.Charisma.score}\nModificator: {char.character.Charisma.modifier}')


def strength_roll():
    modifier = char.character.Strength.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Strength = {d20} + {modifier} = {d20 + modifier}')


def dexterity_roll():
    modifier = char.character.Dexterity.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Dexterity = {d20} + {modifier} = {d20 + modifier}')


def constitution_roll():
    modifier = char.character.Constitution.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Constitution = {d20} + {modifier} = {d20 + modifier}')

def intelligence_roll():
    modifier = char.character.Intelligence.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Intelligence = {d20} + {modifier} = {d20 + modifier}')

def wisdom_roll():
    modifier = char.character.Wisdom.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Wisdom = {d20} + {modifier} = {d20 + modifier}')

def charisma_roll():
    modifier = char.character.Charisma.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Charisma = {d20} + {modifier} = {d20 + modifier}')

ui.strength_button.clicked.connect(strength_roll)
ui.dexterity_button.clicked.connect(dexterity_roll)
ui.constituion_button.clicked.connect(constitution_roll)
ui.intelligence_button.clicked.connect(intelligence_roll)
ui.wisdom_button.clicked.connect(wisdom_roll)
ui.charisma_button.clicked.connect(charisma_roll)

# Main loop
sys.exit(app.exec_())
