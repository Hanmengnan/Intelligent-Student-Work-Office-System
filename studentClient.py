import PyQt5.QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from clientTeacher import perimg
from window import *


class studentWindow(window):
    def __init__(self,width=1366,height=768):
        window.__init__(self,width,height)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window , QColor(1 , 28 , 52))
        self.setPalette(wholepalette)
        wholeLayout=QHBoxLayout()
        teacherLayout=QVBoxLayout()

        background=perimg().newWidget()
        teacherLayout.addWidget(background)

        wordWidget = QWidget()

        wordpalette = QPalette()
        wordpalette.setBrush(QPalette.Background , QBrush(QPixmap("./studentimg/老师留言.png")))

        wordWidget.setPalette(wordpalette)

        # wordLayout=QHBoxLayout()
        # word=QLabel("21222222222222222222")
        #
        # word.setFont(QFont("微软雅黑", 20, QFont.Bold))
        # word.setStyleSheet('color:rgb(207, 214, 218)')
        # wordLayout.addWidget(word)
        #
        # wordWidget.setLayout(wordLayout)

        sayLable = QLabel()
        sayLable.setFixedHeight(700)
        sayLable.setFixedWidth(700)
        img = PyQt5.QtGui.QPixmap('./studentimg/老师留言.png')
        sayLable.setPixmap(img)

        teacherLayout.addWidget(wordWidget)
        wholeLayout.addLayout(teacherLayout)
        tempLable = QLabel()
        tempLable.setFixedHeight(700)
        img = PyQt5.QtGui.QPixmap('./studentimg/11.png')
        tempLable.setPixmap(img)

        wholeLayout.addWidget(tempLable)
        wholeLayout.addWidget(sayLable)
        self.setLayout(wholeLayout)

    def visitorShow(self,visitorList):
        pass




