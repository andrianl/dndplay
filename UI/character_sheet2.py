# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character_sheet.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CharacterSheet(object):
    def setupUi(self, CharacterSheet):
        if not CharacterSheet.objectName():
            CharacterSheet.setObjectName(u"CharacterSheet")
        CharacterSheet.resize(617, 718)
        self.centralwidget = QWidget(CharacterSheet)
        self.centralwidget.setObjectName(u"centralwidget")
        self.abilities = QFrame(self.centralwidget)
        self.abilities.setObjectName(u"abilities")
        self.abilities.setGeometry(QRect(20, 120, 120, 351))
        self.abilities.setFrameShape(QFrame.StyledPanel)
        self.abilities.setFrameShadow(QFrame.Raised)
        self.strength_button = QPushButton(self.abilities)
        self.strength_button.setObjectName(u"strength_button")
        self.strength_button.setGeometry(QRect(20, 10, 75, 23))
        self.dexterity_button = QPushButton(self.abilities)
        self.dexterity_button.setObjectName(u"dexterity_button")
        self.dexterity_button.setGeometry(QRect(20, 40, 75, 23))
        self.constituion_button = QPushButton(self.abilities)
        self.constituion_button.setObjectName(u"constituion_button")
        self.constituion_button.setGeometry(QRect(20, 70, 75, 23))
        self.intelligence_button = QPushButton(self.abilities)
        self.intelligence_button.setObjectName(u"intelligence_button")
        self.intelligence_button.setGeometry(QRect(20, 100, 75, 23))
        self.wisdom_button = QPushButton(self.abilities)
        self.wisdom_button.setObjectName(u"wisdom_button")
        self.wisdom_button.setGeometry(QRect(20, 130, 75, 23))
        self.charisma_button = QPushButton(self.abilities)
        self.charisma_button.setObjectName(u"charisma_button")
        self.charisma_button.setGeometry(QRect(20, 160, 75, 23))
        self.basic = QFrame(self.centralwidget)
        self.basic.setObjectName(u"basic")
        self.basic.setGeometry(QRect(160, 10, 441, 80))
        self.basic.setFrameShape(QFrame.StyledPanel)
        self.basic.setFrameShadow(QFrame.Raised)
        self.cls_lbl = QLabel(self.basic)
        self.cls_lbl.setObjectName(u"cls_lbl")
        self.cls_lbl.setGeometry(QRect(10, 10, 71, 16))
        self.race_lbl = QLabel(self.basic)
        self.race_lbl.setObjectName(u"race_lbl")
        self.race_lbl.setGeometry(QRect(10, 50, 51, 16))
        self.background_lbl = QLabel(self.basic)
        self.background_lbl.setObjectName(u"background_lbl")
        self.background_lbl.setGeometry(QRect(150, 10, 47, 13))
        self.label_4 = QLabel(self.basic)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 50, 47, 13))
        self.label_5 = QLabel(self.basic)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 10, 47, 13))
        self.label_6 = QLabel(self.basic)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 50, 47, 13))
        self.ph = QFrame(self.centralwidget)
        self.ph.setObjectName(u"ph")
        self.ph.setGeometry(QRect(160, 100, 231, 131))
        self.ph.setFrameShape(QFrame.StyledPanel)
        self.ph.setFrameShadow(QFrame.Raised)
        self.armor_class = QLabel(self.ph)
        self.armor_class.setObjectName(u"armor_class")
        self.armor_class.setGeometry(QRect(20, 20, 47, 13))
        self.initiative = QLabel(self.ph)
        self.initiative.setObjectName(u"initiative")
        self.initiative.setGeometry(QRect(100, 20, 47, 13))
        self.speed_2 = QLabel(self.ph)
        self.speed_2.setObjectName(u"speed_2")
        self.speed_2.setGeometry(QRect(170, 20, 47, 13))
        self.hp = QLabel(self.ph)
        self.hp.setObjectName(u"hp")
        self.hp.setGeometry(QRect(100, 60, 47, 13))
        self.hp.setMargin(0)
        self.weapon = QFrame(self.centralwidget)
        self.weapon.setObjectName(u"weapon")
        self.weapon.setGeometry(QRect(160, 260, 231, 211))
        self.weapon.setFrameShape(QFrame.StyledPanel)
        self.weapon.setFrameShadow(QFrame.Raised)
        self.personality = QFrame(self.centralwidget)
        self.personality.setObjectName(u"personality")
        self.personality.setGeometry(QRect(410, 120, 191, 241))
        self.personality.setFrameShape(QFrame.StyledPanel)
        self.personality.setFrameShadow(QFrame.Raised)
        self.proficiencies = QFrame(self.centralwidget)
        self.proficiencies.setObjectName(u"proficiencies")
        self.proficiencies.setGeometry(QRect(20, 490, 120, 161))
        self.proficiencies.setFrameShape(QFrame.StyledPanel)
        self.proficiencies.setFrameShadow(QFrame.Raised)
        self.equipment = QFrame(self.centralwidget)
        self.equipment.setObjectName(u"equipment")
        self.equipment.setGeometry(QRect(160, 490, 231, 161))
        self.equipment.setFrameShape(QFrame.StyledPanel)
        self.equipment.setFrameShadow(QFrame.Raised)
        self.feats = QFrame(self.centralwidget)
        self.feats.setObjectName(u"feats")
        self.feats.setGeometry(QRect(410, 370, 191, 281))
        self.feats.setFrameShape(QFrame.StyledPanel)
        self.feats.setFrameShadow(QFrame.Raised)
        self.dice = QFrame(self.centralwidget)
        self.dice.setObjectName(u"dice")
        self.dice.setGeometry(QRect(20, 10, 120, 80))
        self.dice.setFrameShape(QFrame.StyledPanel)
        self.dice.setFrameShadow(QFrame.Raised)
        self.dice_result = QLabel(self.dice)
        self.dice_result.setObjectName(u"dice_result")
        self.dice_result.setGeometry(QRect(30, 30, 47, 13))
        CharacterSheet.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CharacterSheet)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 617, 21))
        self.menussssss = QMenu(self.menubar)
        self.menussssss.setObjectName(u"menussssss")
        CharacterSheet.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CharacterSheet)
        self.statusbar.setObjectName(u"statusbar")
        CharacterSheet.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menussssss.menuAction())

        self.retranslateUi(CharacterSheet)

        QMetaObject.connectSlotsByName(CharacterSheet)
    # setupUi

    def retranslateUi(self, CharacterSheet):
        CharacterSheet.setWindowTitle(QCoreApplication.translate("CharacterSheet", u"MainWindow", None))
        self.strength_button.setText(QCoreApplication.translate("CharacterSheet", u"Strength", None))
        self.dexterity_button.setText(QCoreApplication.translate("CharacterSheet", u"Dexterity", None))
        self.constituion_button.setText(QCoreApplication.translate("CharacterSheet", u"Constituion", None))
        self.intelligence_button.setText(QCoreApplication.translate("CharacterSheet", u"Intelligence", None))
        self.wisdom_button.setText(QCoreApplication.translate("CharacterSheet", u"Wisdom", None))
        self.charisma_button.setText(QCoreApplication.translate("CharacterSheet", u"Charisma", None))
        self.cls_lbl.setText("")
        self.race_lbl.setText("")
        self.background_lbl.setText("")
        self.label_4.setText(QCoreApplication.translate("CharacterSheet", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("CharacterSheet", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("CharacterSheet", u"TextLabel", None))
        self.armor_class.setText("")
        self.initiative.setText("")
        self.speed_2.setText("")
        self.hp.setText("")
        self.dice_result.setText(QCoreApplication.translate("CharacterSheet", u"0", None))
        self.menussssss.setTitle(QCoreApplication.translate("CharacterSheet", u"Menu", None))
    # retranslateUi

