from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QMainWindow
from PyQt5.QtCore import Qt
from ui import Ui_Form
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def keyPressEvent(self, e): 
        Form = Window()
        ui = Ui_Form()
        ui.setupUi(Form)
        if e.key() == Qt.Key_0:
            settext(0)
        if e.key() == Qt.Key_1:
            settext(1)
        if e.key() == Qt.Key_2:
            settext(2)
        if e.key() == Qt.Key_3:
            settext(3)
        if e.key() == Qt.Key_4:
            settext(4)
        if e.key() == Qt.Key_5:
            settext(5)
        if e.key() == Qt.Key_6:
            settext(6)
        if e.key() == Qt.Key_7:
            settext(7)
        if e.key() == Qt.Key_8:
            settext(8)
        if e.key() == Qt.Key_9:
            settext(9)
        if e.key() == Qt.Key_Plus:
            settext('+')
        if e.key() == Qt.Key_Minus:
            settext('-')
        if e.key() == Qt.Key_Enter:
            dorivnye()
        if e.key() ==  16777220:
            dorivnye()
        if e.key() == Qt.Key_Backspace:
            deltext()
        if e.key() == 42:
            settext('*')
        if e.key() == 47:
            settext('/')
        if e.key() == 40:
            settext('(')
        if e.key() == 41:
            settext(')')
        if e.key() == Qt.Key_Delete:
            clearall()
        if e.key() == 46:
            settext('.')
app = QtWidgets.QApplication(sys.argv)
Form = Window()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
#main code
def settext(txt):
    x = ui.lineEdit.displayText()
    ui.lineEdit.setText(x+str(txt))

def deltext():
    x = ui.lineEdit.displayText()
    a = list(x)
    z = len(a)
    z =z-1
    try:
        del a[z]
        listToStr = ''.join([str(elem) for elem in a])
        ui.lineEdit.setText(str(listToStr))
    except IndexError:
        pass
def clearall():
    ui.lineEdit.setText('')
def dorivnye():
    try:
        x = eval(ui.lineEdit.displayText())
        ui.lineEdit.setText(str(x))
    except SyntaxError:
        pass
ui.button_0.clicked.connect(lambda:settext(0))
ui.button_1.clicked.connect(lambda:settext(1))
ui.button_2.clicked.connect(lambda:settext(2))
ui.button_3.clicked.connect(lambda:settext(3))
ui.button_4.clicked.connect(lambda:settext(4))
ui.button_5.clicked.connect(lambda:settext(5))
ui.button_6.clicked.connect(lambda:settext(6))
ui.button_7.clicked.connect(lambda:settext(7))
ui.button_8.clicked.connect(lambda:settext(8))
ui.button_9.clicked.connect(lambda:settext(9))
ui.button_minus.clicked.connect(lambda:settext('-'))
ui.button_plus.clicked.connect(lambda:settext('+'))
ui.button_pomnosh.clicked.connect(lambda:settext('*'))
ui.button_podilutu.clicked.connect(lambda:settext('/'))
ui.button_koma.clicked.connect(lambda:settext('.'))
ui.pushButton.clicked.connect(lambda:settext('('))
ui.pushButton_2.clicked.connect(lambda:settext(')'))
ui.button_delete.clicked.connect(lambda:deltext())
ui.button_clear.clicked.connect(lambda:clearall())
ui.button_dorivnye.clicked.connect(lambda:dorivnye())

#start gui
app.exec_()
