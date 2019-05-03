import PyQt5.QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from clock import *
from window import *
class doorWindow(window):
    def __init__(self,width=1366, height=768):
        window.__init__(self,width=1366,height=768)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1,28,52))
        self.setPalette(wholepalette)
        clientStudentLayout = QVBoxLayout()
        duoyuLable = QLabel()
        duoyuLable.setFixedHeight(100)
        clientStudentLayout.addWidget(duoyuLable)
        teacherDataLayout=QHBoxLayout()
        background1 = QWidget()
        background1.setFixedHeight(550)
        background1.setFixedWidth(400)
        background1.setStyleSheet('QWidget{border-image:url(./doorimg/图层 3.png);}')
        backgroundLayout = QVBoxLayout()
        background = QWidget()
        background.setFixedHeight(530)
        background.setFixedWidth(380)
        background.setStyleSheet("QWidget{border-image:url(./doorimg/图层 4.png);}")
        backgroundLayout.addWidget(background)
        background1.setLayout(backgroundLayout)
        teacherDataLayout.addWidget(background1)
        self.kuang = QLabel()
        self.kuang.setFixedWidth(930)
        self.kuang.setFixedHeight(650)
        img = PyQt5.QtGui.QPixmap('./doorimg/框.png')
        self.kuang.setPixmap(img)
        teacherDataLayout.addWidget(self.kuang)
        dataLayout=QVBoxLayout()
        self.lableList=[]
        for i in range(3):
            welcomeText=QLabel()
            self.lableList.append(welcomeText)
            welcomeText.setText("""同 学 欢迎你，
            辅导员 辅 导 员 正在等你""")
            welcomeText.setAlignment(Qt.AlignLeft)
            welcomeText.setGeometry(QRect(330, 220, 200, 70))
            welcomeText.setFont(QFont("微软雅黑", 20, QFont.Bold))
            welcomeText.setStyleSheet('color:rgb(207, 214, 218)')
            welcomeText.setFixedHeight(100)
            dataLayout.addWidget(welcomeText)
            xian = QLabel()
            img = PyQt5.QtGui.QPixmap('./doorimg/线.png')
            xian.setPixmap(img)
            dataLayout.addWidget(xian)
        teacherDataLayout.addLayout(dataLayout)
        clientStudentLayout.addLayout(teacherDataLayout)
        titleLayout=QHBoxLayout()
        titleRightImg = QLabel()
        titleRightImg.setFixedWidth(405)
        img = PyQt5.QtGui.QPixmap('./doorimg/图层 4.2.png')
        titleRightImg.setPixmap(img)
        titleLayout.addWidget(titleRightImg)
        titleImg = QLabel()
        img = PyQt5.QtGui.QPixmap('./doorimg/信息学院智能学工.png')
        titleImg.setPixmap(img)
        titleLayout.addWidget(titleImg)
        titleLeftImg = QLabel()
        titleLeftImg.setFixedWidth(405)
        img = PyQt5.QtGui.QPixmap('./doorimg/图层 4.1.png')
        titleLeftImg.setPixmap(img)
        titleLayout.addWidget(titleLeftImg)
        clientStudentLayout.addLayout(titleLayout)
        self.setLayout(clientStudentLayout)
        self.showFullScreen()
    def visitorShow(self,visitorList):
        for i in visitorList:
            text=visitorList["name"]+ "欢迎你，"+"\n辅导员 "+visitorList["teacher"]+" 正在等你"
            self.lableList[list(visitorList).index(i)].setText(text)
        teacherName=visitorList["teacher"]
        img = PyQt5.QtGui.QPixmap('./doorimg/+'+teacherName+'.png')
        self.kuang.setPixmap(img)
