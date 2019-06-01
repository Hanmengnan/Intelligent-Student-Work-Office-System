import PyQt5.QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from window import *
class doorWindow(window):
    lableList = []

    def __init__(self,width=3340, height=1440):
        window.__init__(self,width=3340,height=1440)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1,28,52))
        self.setPalette(wholepalette)
        #全局背景
        wholeLayout = QVBoxLayout()
        #全局布局
        tempLable = QLabel()
        wholeLayout.addWidget(tempLable)
        #全局布局


        studentDataLayout=QHBoxLayout()
        #上半部分布局
        background = QWidget()
        background.setFixedHeight(850)
        background.setFixedWidth(600)
        background.setStyleSheet('QWidget{border-image:url(./doorimg/图层 3.png);}')
        #头像背景区域
        perimg = QWidget()
        perimg.setFixedHeight(815)
        perimg.setFixedWidth(580)
        perimg.setStyleSheet("QWidget{border-image:url(./doorimg/图层 4.png);}")
        #头像区域
        perimgLayout = QVBoxLayout()
        perimgLayout.addWidget(perimg)
        #头像区域布局
        background.setLayout(perimgLayout)
        studentDataLayout.addWidget(background)

        self.seat = QLabel()
        seatimg = PyQt5.QtGui.QPixmap('./doorimg/框.png')
        self.seat.setPixmap(seatimg)
        studentDataLayout.addWidget(self.seat)
        #座位图区域

        welcomeLayout=QVBoxLayout()
        for i in range(3):
            welcomeText=QLabel()
            self.lableList.append(welcomeText)
            welcomeText.setText("")
            welcomeText.setAlignment(Qt.AlignHCenter)
            welcomeText.setGeometry(QRect(330, 220, 200, 70))
            welcomeText.setFont(QFont("微软雅黑", 50, QFont.Bold))
            welcomeText.setStyleSheet('color:rgb(207, 214, 218)')
            welcomeLayout.addWidget(welcomeText)
            line = QLabel()
            lineimg = PyQt5.QtGui.QPixmap('./doorimg/线.png')
            line.setPixmap(lineimg)
            welcomeLayout.addWidget(line)
        #欢迎语区域
        studentDataLayout.addLayout(welcomeLayout)
        wholeLayout.addLayout(studentDataLayout)
        #上半部分结束

        titleLayout=QHBoxLayout()

        titleRightImg = QLabel()
        img = PyQt5.QtGui.QPixmap('./doorimg/图层 4.4.png')
        titleRightImg.setPixmap(img)
        titleLayout.addWidget(titleRightImg)
        #下部分左侧

        titleImg = QLabel()
        img = PyQt5.QtGui.QPixmap('./doorimg/信息学院智能学工.png')
        titleImg.setPixmap(img)
        titleLayout.addWidget(titleImg)
        #下部分中间

        titleLeftImg = QLabel()
        img = PyQt5.QtGui.QPixmap('./doorimg/图层 4.3.png')
        titleLeftImg.setPixmap(img)
        titleLayout.addWidget(titleLeftImg)
        #下部分右侧

        wholeLayout.addLayout(titleLayout)
        #加入下半部分

        self.setLayout(wholeLayout)
        self.showFullScreen()

    def visitorShow(self,visitorList):
        """
        来访者显示
        :param visitorList:
        :return:
        """
        for i in (visitorList):
            name=""
            for letter in i["xm"]:
                name+=letter
                name+=" "
            text=name+ "  欢迎你"+"\n\t辅导员 "+i["js"]+" 正在等你"
            self.lableList[visitorList.index(i)].setText(text)

    def visitorDelete(self):
        """
        清空函数
        :return:
        """
        for i in range(3):
            self.lableList[i].setText("")



