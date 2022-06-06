import sys
import os
import socket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from chatbox_server import serv
class UI_class(QDialog):
    def __init__(self):
        super(UI_class,self).__init__()
        loadUi("chatbox_gui.ui",self)
        self.setWindowTitle('Chatbox')
        # defining widgets
        self.label=self.findChild(QLabel,'label')
        self.textedit=self.findChild(QTextEdit,'textEdit')
        self.button=self.findChild(QPushButton,'pushButton')
        self.plainEdit=self.findChild(QPlainTextEdit,'plainTextEdit')
        self.show()
        self.button.clicked.connect(lambda: self.clicker())
        # doing something
    def clicker(self):
        self.plainEdit.append('\n'+'You: '+ self.textedit.text())
        serv.send(bytes(self.sendtext.text(),'utf-8'))

app=QApplication(sys.argv)
UIWindow=UI_class()
app.exec_()
serv.close()