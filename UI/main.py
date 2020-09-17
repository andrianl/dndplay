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

ui.cls_lbl.setText(f'Class: {char.Andy.clss.name}')
ui.race_lbl.setText(f'Race: {char.Andy.Race.name}')
ui.background_lbl.setText(f'Background: {char.Andy.background.name}')



ui.initiative.setText(f'Initiative: {char.Andy.initiative}')
ui.hp.setText(f'HP: {char.Andy.max_health_point}')
ui.speed.setText(f'Speed: {char.Andy.speed}')
ui.armor_class.setText(f'Armor Class: {char.Andy.armor_class}')



ui.strength_button.setText(f'Strength: {char.Andy.Strength.score}\nModificator: {char.Andy.Strength.modifier}')
ui.dexterity_button.setText(f'Dexterity: {char.Andy.Dexterity.score}\nModificator: {char.Andy.Dexterity.modifier}')
ui.constituion_button.setText(f'Constitution: {char.Andy.Constitution.score}\nModificator: {char.Andy.Constitution.modifier}')
ui.intelligence_button.setText(f'Intelligence: {char.Andy.Intelligence.score}\nModificator: {char.Andy.Intelligence.modifier}')
ui.wisdom_button.setText(f'Wisdom: {char.Andy.Wisdom.score}\nModificator: {char.Andy.Wisdom.modifier}')
ui.charisma_button.setText(f'Charisma: {char.Andy.Charisma.score}\nModificator: {char.Andy.Charisma.modifier}')


def strength_roll():
    modifier = char.Andy.Strength.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Strength = {d20} + {modifier} = {d20 + modifier}')


def dexterity_roll():
    modifier = char.Andy.Dexterity.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Dexterity = {d20} + {modifier} = {d20 + modifier}')


def constitution_roll():
    modifier = char.Andy.Constitution.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Constitution = {d20} + {modifier} = {d20 + modifier}')

def intelligence_roll():
    modifier = char.Andy.Intelligence.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Intelligence = {d20} + {modifier} = {d20 + modifier}')

def wisdom_roll():
    modifier = char.Andy.Wisdom.modifier
    d20 = dice.Dice.roll([1, 20])
    ui.dice_result.setText(f'D20 + Wisdom = {d20} + {modifier} = {d20 + modifier}')

def charisma_roll():
    modifier = char.Andy.Charisma.modifier
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
