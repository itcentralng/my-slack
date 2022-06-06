from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
import sys
from chatbox_client import clientt
class UI(QDialog):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("chatbox_gui.ui",self)
        self.setWindowTitle('Chatbox')
        self.boxx=self.findChild(QLineEdit,'sendbox')
        self.button=self.findChild(QPushButton,'pushButton')
        self.plainEdit=self.findChild(QTextEdit,'screen')
        self.show()
        self.button.clicked.connect(lambda: self.clicker())
        self.plainEdit.setText('place holder')
        # doing something
        # while 1:
        #     incoming_message=clientt.recv(1024)
        #     incoming_message=incoming_message.decode()
        #     self.plainEdit.append('\n'+'Them: ' + incoming_message)

    def clicker(self):
        # clientt.send(bytes(self.label.text(),'utf-8'))
        msg = self.boxx.text()
        clientt.send(bytes(msg,'utf-8'))
        self.plainEdit.append('\n'+'You: ' + msg)
        print('there is some sort of error')
        print(clientt.recv(1024).decode())
    
    # def wee(self, msg):
    #     self.plainEdit.append('\n'+'Them: ' + msg)
        

app=QApplication(sys.argv)
UIWindow=UI()
app.exec_()
# while 1:
#     incoming_message=clientt.recv(1024)
#     incoming_message=incoming_message.decode()
#     print(incoming_message)
#     # UIWindow.wee(incoming_message)
clientt.close()