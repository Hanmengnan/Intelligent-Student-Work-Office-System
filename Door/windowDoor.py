import PyQt5.QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Door.window import *
class doorWindow(window):
    def __init__(self,width=3340, height=1440):
        window.__init__(self,width=3340,height=1440)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1,28,52))
        self.setPalette(wholepalette)
        wholeLayout = QVBoxLayout()
        tempLable = QLabel()
        #tempLable.setFixedHeight(100)
        wholeLayout.addWidget(tempLable)
        studentDataLayout=QHBoxLayout()
        background = QWidget()
        background.setFixedHeight(850)
        background.setFixedWidth(600)
        background.setStyleSheet('QWidget{border-image:url(./doorimg/图层 3.png);}')
        perimgLayout = QVBoxLayout()
        perimg = QWidget()
        perimg.setFixedHeight(815)
        perimg.setFixedWidth(580)
        perimg.setStyleSheet("QWidget{border-image:url(./doorimg/图层 4.png);}")
        perimgLayout.addWidget(perimg)
        background.setLayout(perimgLayout)
        studentDataLayout.addWidget(background)
        self.seat = QLabel()
        # self.seat.setFixedWidth(930)
        # self.seat.setFixedHeight(650)
        seatimg = PyQt5.QtGui.QPixmap('./doorimg/框.png')
        self.seat.setPixmap(seatimg)
        studentDataLayout.addWidget(self.seat)
        welcomeLayout=QVBoxLayout()
        self.lableList=[]
        for i in range(3):
            welcomeText=QLabel()
            self.lableList.append(welcomeText)
            welcomeText.setText("")
            welcomeText.setAlignment(Qt.AlignHCenter)
            welcomeText.setGeometry(QRect(330, 220, 200, 70))
            welcomeText.setFont(QFont("微软雅黑", 50, QFont.Bold))
            welcomeText.setStyleSheet('color:rgb(207, 214, 218)')
            # welcomeText.setFixedHeight(100)
            welcomeLayout.addWidget(welcomeText)
            line = QLabel()
            lineimg = PyQt5.QtGui.QPixmap('./doorimg/线.png')
            line.setPixmap(lineimg)
            welcomeLayout.addWidget(line)
        studentDataLayout.addLayout(welcomeLayout)
        wholeLayout.addLayout(studentDataLayout)
        titleLayout=QHBoxLayout()
        titleRightImg = QLabel()
        #titleRightImg.setFixedWidth(405)
        img = PyQt5.QtGui.QPixmap('./doorimg/图层 4.4.png')
        titleRightImg.setPixmap(img)
        titleLayout.addWidget(titleRightImg)
        titleImg = QLabel()
        img = PyQt5.QtGui.QPixmap('./doorimg/信息学院智能学工.png')
        
        titleImg.setPixmap(img)
        titleLayout.addWidget(titleImg)
        titleLeftImg = QLabel()
        #titleLeftImg.setFixedWidth(405)
        img = PyQt5.QtGui.QPixmap('./doorimg/图层 4.3.png')
        titleLeftImg.setPixmap(img)
        titleLayout.addWidget(titleLeftImg)
        wholeLayout.addLayout(titleLayout)
        self.setLayout(wholeLayout)
        self.showFullScreen()
    def visitorShow(self,visitorList):
        for i in (visitorList):
            name=""
            for letter in i["xm"]:
                name+=letter
                name+=" "
            text=name+ "  欢迎你"+"\n\t辅导员 "+i["js"]+" 正在等你"
            try:
                self.lableList[visitorList.index(i)].setText(text)
            except:
                pass
    def visitorDelete(self):
        for i in range(3):
            self.lableList[i].setText("")



