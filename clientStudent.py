from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import PyQt5.QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor

from window import *
from PyQt5.QtWidgets import *
from clock import *


class studentWindow(window):
    def __init__(self,width=1366, height=768):
        window.__init__(self,width=1366,height=768)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1,28,52))
        self.setPalette(wholepalette)
        clientStudentLayout = QVBoxLayout()
        #1总布局
        teacherDataLayout=QHBoxLayout()
        #1.1上层布局
        background1 = QWidget()
        # 1.1.1.1 最下背景
        background1.setFixedHeight(450)
        background1.setFixedWidth(300)
        background1.setStyleSheet("QWidget{border-image:url(./img/图层 2.png);}")

        background2Layout = QVBoxLayout()
        #1.1.1.1.2 中层背景
        background2=QWidget()
        background2.setFixedHeight(430)
        background2.setFixedWidth(280)
        background2.setStyleSheet("QWidget{border-image:url(./img/图层 3.png);}")
        background2Layout.addWidget(background2)
        background1.setLayout(background2Layout)
        teacherDataLayout.addWidget(background1)
        #加入1.1.1

        kuang = QLabel()
        #1.1.2
        kuang.setFixedWidth(800)
        kuang.setFixedHeight(650)
        img = PyQt5.QtGui.QPixmap('./img/框.png')
        kuang.setPixmap(img)
        teacherDataLayout.addWidget(kuang)

        dataLayout=QVBoxLayout()
        xian = QLabel()
        #1.1.3
        xian.setFixedHeight(650)
        img = PyQt5.QtGui.QPixmap('./img/线.png')
        xian.setPixmap(img)
        teacherDataLayout.addWidget(xian)

        clientStudentLayout.addLayout(teacherDataLayout)
        # # 加入1.1





        titleLayout=QHBoxLayout()
        #1.2
        titleRightImg = QLabel()
        titleRightImg.setFixedWidth(405)
        # 1.2.1
        img = PyQt5.QtGui.QPixmap('./img/图层 4.2.png')
        titleRightImg.setPixmap(img)
        titleLayout.addWidget(titleRightImg)
        #加入1.2.1

        titleImg = QLabel()
        # 1.2.2
        img = PyQt5.QtGui.QPixmap('./img/信息学院智能学工.png')
        titleImg.setPixmap(img)
        titleLayout.addWidget(titleImg)
        #加入1.2.2
        titleLeftImg = QLabel()
        #1.2.3
        titleLeftImg.setFixedWidth(405)
        img = PyQt5.QtGui.QPixmap('./img/图层 4.1.png')
        titleLeftImg.setPixmap(img)
        titleLayout.addWidget(titleLeftImg)
        #加入1.2.3
        clientStudentLayout.addLayout(titleLayout)
        #加入1.2
        self.setLayout(clientStudentLayout)
        #设置总布局

