import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget


class window(QWidget):
    def __init__(self,width,height):
        super(window,self).__init__()
        self.windowDef(width,height)
    def windowDef(self,width,height):
        self.setGeometry(0,0,width,height)
        frame= self.frameGeometry()
        center= PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())
        self.setWindowTitle("信息学院学工办终端")
        self.setWindowIcon(QIcon("icon.jpg"))