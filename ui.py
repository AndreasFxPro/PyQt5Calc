# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
class Ui_Form(object):
    def setupUi(self, BoykoCalc):
        BoykoCalc.setObjectName("BoykoCalc")
        BoykoCalc.resize(320, 335)
        BoykoCalc.setStyleSheet("QPushButton{\n"
"height: 48px;\n"
"width:  48px;\n"
"font-size: 20px;\n"
"    background-color: rgb(230, 230, 250);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(236, 230, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QLineEdit{\n"
"font-size: 30px;\n"
"}"
)
        self.gridLayoutWidget = QtWidgets.QWidget(BoykoCalc)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 320, 306))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 2, 0, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 3, 0, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_5.setIconSize(QtCore.QSize(50, 16))
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 2, 1, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 2, 2, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 4, 1, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 3, 2, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 1, 2, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 3, 1, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 1, 1, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 1, 0, 1, 1)
        self.button_podilutu = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_podilutu.setObjectName("button_podilutu")
        self.gridLayout.addWidget(self.button_podilutu, 0, 3, 1, 1)
        self.button_pomnosh = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_pomnosh.setObjectName("button_pomnosh")
        self.gridLayout.addWidget(self.button_pomnosh, 1, 3, 1, 1)
        self.button_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 3, 3, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 2, 3, 1, 1)
        self.button_dorivnye = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_dorivnye.setObjectName("button_dorivnye")
        self.gridLayout.addWidget(self.button_dorivnye, 4, 3, 1, 1)
        self.button_koma = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_koma.setObjectName("button_koma")
        self.gridLayout.addWidget(self.button_koma, 4, 2, 1, 1)
        self.button_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 4, 0, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(BoykoCalc)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 321, 31))
        self.lineEdit.setInputMask("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(BoykoCalc)
        QtCore.QMetaObject.connectSlotsByName(BoykoCalc)
    def retranslateUi(self, BoykoCalc):
        _translate = QtCore.QCoreApplication.translate
        BoykoCalc.setWindowTitle(_translate("BoykoCalc", "BoykoCalc"))
        self.button_4.setText(_translate("BoykoCalc", "4"))
        self.button_1.setText(_translate("BoykoCalc", "1"))
        self.button_5.setText(_translate("BoykoCalc", "5"))
        self.button_6.setText(_translate("BoykoCalc", "6"))
        self.button_0.setText(_translate("BoykoCalc", "0"))
        self.button_3.setText(_translate("BoykoCalc", "3"))
        self.button_9.setText(_translate("BoykoCalc", "9"))
        self.button_2.setText(_translate("BoykoCalc", "2"))
        self.button_8.setText(_translate("BoykoCalc", "8"))
        self.button_7.setText(_translate("BoykoCalc", "7"))
        self.button_podilutu.setText(_translate("BoykoCalc", "/"))
        self.button_pomnosh.setText(_translate("BoykoCalc", "*"))
        self.button_plus.setText(_translate("BoykoCalc", "+"))
        self.button_minus.setText(_translate("BoykoCalc", "-"))
        self.button_dorivnye.setText(_translate("BoykoCalc", "="))
        self.button_koma.setText(_translate("BoykoCalc", ","))
        self.button_clear.setText(_translate("BoykoCalc", "Clear"))
        self.button_delete.setText(_translate("BoykoCalc", "Delete"))
        self.pushButton.setText(_translate("BoykoCalc", "("))
        self.pushButton_2.setText(_translate("BoykoCalc", ")"))
