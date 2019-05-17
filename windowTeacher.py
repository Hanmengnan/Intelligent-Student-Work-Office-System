import PyQt5.QtCore
from PyQt5 import QtCore
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap , QPalette
from PyQt5.QtWidgets import *
from window import *
from settings import *
class perimg(QWidget):
    def __init__(self):
        QWidget.__init__(self)
    def newWidget(self):
        background=QWidget()
        background.setFixedHeight(390)
        background.setFixedWidth(500)
        background.setStyleSheet('QWidget{border-image:url(./teacherimg/头像区域.png);}')
        perimgLayout = QVBoxLayout()
        perimg = QWidget()
        perimg.setFixedHeight(330)
        perimg.setFixedWidth(320)
        perimg.setStyleSheet("QWidget{border-image:url(./teacherimg/头像.png);}")
        perimgLayout.setAlignment(QtCore.Qt.AlignCenter)
        perimgLayout.addWidget(perimg)
        background.setLayout(perimgLayout)
        return background

class teacherWindow(window):
    def __init__(self, width=1366, height=768):
        window.__init__(self, width, height)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1, 28, 52))
        self.setPalette(wholepalette)

        wholeLayout=QHBoxLayout()
        studentDataLayout=QVBoxLayout()
        background = perimg().newWidget()
        studentDataLayout.addWidget(background)

        self.data = QWidget()
        self.data.setFixedWidth(444)
        self.data.setFixedHeight(355)
        self.data.setAutoFillBackground(True)
        datapalette = QPalette()
        datapalette.setBrush(QPalette.Background, QBrush(QPixmap("./teacherimg/信息.png")))
        self.data.setPalette(datapalette)

        dataBackgroundLayout=QHBoxLayout()
        tempLable=QLabel()
        tempLable.setFixedWidth(130)
        tempLable.setFixedHeight(350)
        dataBackgroundLayout.addWidget(tempLable)

        dataLayout=QVBoxLayout()

        self.nameLable=QLabel("***")
        self.nameLable.setFixedHeight(190)
        self.nameLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.nameLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout.addWidget(self.nameLable)

        self.classLable = QLabel("*****")
        self.classLable.setFixedHeight(170)
        self.classLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.classLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout.addWidget(self.classLable)

        self.numLable = QLabel("***********")
        self.numLable.setFixedHeight(140)
        self.numLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.numLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout.addWidget(self.numLable)

        self.phoneLable = QLabel("***********")
        self.phoneLable.setFixedHeight(110)
        self.phoneLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.phoneLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout.addWidget(self.phoneLable)

        dataBackgroundLayout.addLayout(dataLayout)
        self.data.setLayout(dataBackgroundLayout)

        studentDataLayout.addWidget(self.data)

        wholeLayout.addLayout(studentDataLayout)

        tempLable = QLabel()
        tempLable.setFixedWidth(200)
        img = PyQt5.QtGui.QPixmap('./teacherimg/分隔.png')
        tempLable.setPixmap(img)
        wholeLayout.addWidget(tempLable)

        visitorData=self.gradeData()

        visitorRecord = QWidget()
        visitorRecord.setStyleSheet("QWidget{border-image:url(./teacherimg/STARS.png);}")
        visitorRecord.setLayout(visitorData)

        wholeLayout.addWidget(visitorRecord)

        self.setLayout(wholeLayout)
        # self.showFullScreen()
    def gradeData(self):

        visitorListLayout=QVBoxLayout()
        titleLayout = QGridLayout()

        visitor = QLabel()
        img = PyQt5.QtGui.QPixmap('./teacherimg/访客记录.png')
        visitor.setPixmap(img)
        titleLayout.addWidget(visitor , 0 , 1)
        name = QLabel()
        img = PyQt5.QtGui.QPixmap('./teacherimg/姓名.png')
        name.setPixmap(img)
        titleLayout.addWidget(name , 1 , 0)
        time = QLabel()
        img = PyQt5.QtGui.QPixmap('./teacherimg/时间.png')
        time.setPixmap(img)
        titleLayout.addWidget(time , 1 , 1)
        detail = QLabel()
        img = PyQt5.QtGui.QPixmap('./teacherimg/详细.png')
        detail.setPixmap(img)
        titleLayout.addWidget(detail , 1 , 2)
        visitorListLayout.addLayout(titleLayout)

        self.visitorTableWidge = QTableWidget()
        self.visitorTableWidge.setRowCount(TEACHER_VISITOR_ITEM)
        self.visitorTableWidge.setColumnCount(3)
        self.visitorTableWidge.verticalHeader().setVisible(False)
        self.visitorTableWidge.horizontalHeader().setVisible(False)
        self.visitorTableWidge.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.visitorTableWidge.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.buttonList = []
        self.funcList=[]
        for i in range(TEACHER_VISITOR_ITEM):
            button=QPushButton("显示")
            button.setDown(True)
            button.setStyleSheet('QPushButton{color:rgb(67,197,254)}')
            button.setEnabled(False)
            self.buttonList.append(button)
            self.funcList.append(self.makeFunc(i))
            self.visitorTableWidge.setCellWidget(i,2,button)
        visitorListLayout.addWidget(self.visitorTableWidge)
        return visitorListLayout

    def visitorShow(self,visitorList):
        self.visitorList=visitorList
        #便于传参
        for index in range(TEACHER_VISITOR_ITEM):
            self.visitorTableWidge.setItem(index,0,QTableWidgetItem(""))
            self.visitorTableWidge.setItem(index,1,QTableWidgetItem(""))
        for index in range(len(visitorList)):
            #列表显示
            name=QTableWidgetItem(str(visitorList[index]["xm"]))
            name.setForeground(QBrush(QColor(255 ,255 ,255 )))
            self.visitorTableWidge.setItem(index,0,name)
            num = QTableWidgetItem(str(visitorList[index]["xh"]))
            num.setForeground(QBrush(QColor(255 , 255 , 255)))
            self.visitorTableWidge.setItem(index,1,num)
            self.buttonList[index].setEnabled(True)
            self.buttonList[index].clicked.connect(self.funcList[index])
            #不要使用lambda表达式，会延迟函数的执行，导致出错


    def makeFunc(self,index):
        def detailShow():
            studentData=self.visitorList[index]
            self.nameLable.setText(str(studentData["xm"]))
            self.numLable.setText(str(studentData["xh"]))
            self.classLable.setText(studentData["bj"])
            self.phoneLable.setText(studentData["ss"])
        return detailShow
    def visitorDelete(self):
        for index in range(TEACHER_VISITOR_ITEM):
            self.visitorTableWidge.setItem(index , 0 , QTableWidgetItem(""))
            self.visitorTableWidge.setItem(index , 1 , QTableWidgetItem(""))