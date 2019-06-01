import PyQt5.QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *

from window import *


class studentWindow(window):
    def __init__(self,width=1366,height=768):
        window.__init__(self,width,height)
        wholepalette = PyQt5.QtGui.QPalette()
        wholepalette.setColor(PyQt5.QtGui.QPalette.Window , QColor(1 , 28 , 52))
        self.setPalette(wholepalette)
        # 设置全局背景
        wholeLayout=QHBoxLayout()
        #全局布局
        perImgbackground = QWidget()
        perImgbackground.setFixedHeight(500)
        perImgbackground.setFixedWidth(400)
        perImgbackground.setStyleSheet('QWidget{border-image:url(./teacherimg/头像区域.png);}')
        #头像背景区域
        perimg = QWidget()
        perimg.setFixedHeight(400)
        perimg.setFixedWidth(320)
        perimg.setStyleSheet("QWidget{border-image:url(./teacherimg/头像.png);}")
        perimgLayout = QVBoxLayout()
        perimgLayout.setAlignment(QtCore.Qt.AlignCenter)
        # 头像区域
        perimgLayout.addWidget(perimg)
        perImgbackground.setLayout(perimgLayout)
        wholeLayout.addWidget(perImgbackground)
        #加入头像区域
        tempLable = QLabel()
        tempLable.setFixedHeight(700)
        img = PyQt5.QtGui.QPixmap('./studentimg/11.png')
        tempLable.setPixmap(img)
        wholeLayout.addWidget(tempLable)
        #加入占位区域
        wordLable = QLabel()
        wordLable.setFixedHeight(700)
        wordLable.setFixedWidth(700)
        img = PyQt5.QtGui.QPixmap('./studentimg/老师留言.png')
        wordLable.setPixmap(img)
        wholeLayout.addWidget(wordLable)
        #加入留言区域
        self.setLayout(wholeLayout)






