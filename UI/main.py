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

def strength_roll(modifier):
    modifier = char.Andy.Strength.modifier
    ui.dice_result.setText(f'{dice.Dice.roll([1, 20]) + modifier}')

def dexterity_roll(modifier):
    modifier = char.Andy.Dexterity.modifier
    ui.dice_result.setText(f'{dice.Dice.roll([1, 20]) + modifier}')

def constitution_roll(modifier):
    modifier = char.Andy.Constitution.modifier
    ui.dice_result.setText(f'{dice.Dice.roll([1, 20]) + modifier}')

def intelligence_roll(modifier):
    modifier = char.Andy.Intelligence.modifier
    ui.dice_result.setText(f'{dice.Dice.roll([1, 20]) + modifier}')

def wisdom_roll(modifier):
    modifier = char.Andy.Wisdom.modifier
    ui.dice_result.setText(f'{dice.Dice.roll([1, 20]) + modifier}')

def charisma_roll(modifier):
    modifier = char.Andy.Charisma.modifier
    ui.dice_result.setText(f'{dice.Dice.roll([1, 20]) + modifier}')

ui.strength_button.clicked.connect(strength_roll)
ui.dexterity_button.clicked.connect(dexterity_roll)
ui.constituion_button.clicked.connect(constitution_roll)
ui.intelligence_button.clicked.connect(intelligence_roll)
ui.wisdom_button.clicked.connect(wisdom_roll)
ui.charisma_button.clicked.connect(charisma_roll)

# Main loop
sys.exit(app.exec_())
