import PyQt5.QtCore
from PyQt5 import QtCore
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap , QPalette
from PyQt5.QtWidgets import *
from window import *
class teacherWindow(window):
    def __init__(self, width=1366, height=768):
        window.__init__(self, width, height)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1, 28, 52))
        self.setPalette(wholepalette)
        clientTeacherLayout=QHBoxLayout()
        studentDataLayout=QVBoxLayout()

        background1 = QWidget()
        background1.setFixedHeight(390)
        background1.setStyleSheet('QWidget{border-image:url(./teacherimg/头像区域.png);}')
        backgroundLayout = QVBoxLayout()
        background = QWidget()
        background.setFixedHeight(379)
        background.setFixedWidth(300)
        background.setStyleSheet("QWidget{border-image:url(./teacherimg/头像.png);}")
        backgroundLayout.setAlignment(QtCore.Qt.AlignCenter)
        backgroundLayout.addWidget(background)
        background1.setLayout(backgroundLayout)

        studentDataLayout.addWidget(background1)
        self.data = QWidget()
        self.data.setAutoFillBackground(True)
        datapalette = QPalette()
        datapalette.setBrush(QPalette.Background, QBrush(QPixmap("./teacherimg/信息.png")))
        self.data.setPalette(datapalette)
        self.data.setFixedWidth(444)
        self.data.setFixedHeight(355)
        dataLayout1=QHBoxLayout()
        tempLable=QLabel()
        tempLable.setFixedWidth(130)
        tempLable.setFixedHeight(350)
        dataLayout1.addWidget(tempLable)
        dataLayout2=QVBoxLayout()
        self.nameLable=QLabel("***")
        self.nameLable.setFixedHeight(190)
        self.nameLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.nameLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout2.addWidget(self.nameLable)
        self.classLable = QLabel("*****")
        self.classLable.setFixedHeight(170)
        self.classLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.classLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout2.addWidget(self.classLable)
        self.numLable = QLabel("***********")
        self.numLable.setFixedHeight(140)
        self.numLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.numLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout2.addWidget(self.numLable)
        self.phoneLable = QLabel("***********")
        self.phoneLable.setFixedHeight(110)
        self.phoneLable.setFont(QFont("微软雅黑", 20, QFont.Bold))
        self.phoneLable.setStyleSheet('color:rgb(207, 214, 218)')
        dataLayout2.addWidget(self.phoneLable)
        dataLayout1.addLayout(dataLayout2)
        self.data.setLayout(dataLayout1)
        studentDataLayout.addWidget(self.data)
        clientTeacherLayout.addLayout(studentDataLayout)
        fenge = QLabel()
        fenge.setFixedWidth(200)
        img = PyQt5.QtGui.QPixmap('./teacherimg/分隔.png')
        fenge.setPixmap(img)
        clientTeacherLayout.addWidget(fenge)
        visitorData=self.gradeData()
        visitorRecord = QWidget()
        visitorRecord.setStyleSheet("QWidget{border-image:url(./teacherimg/STARS.png);}")
        visitorRecord.setLayout(visitorData)
        clientTeacherLayout.addWidget(visitorRecord)
        self.setLayout(clientTeacherLayout)
        # self.showFullScreen()
    def gradeData(self):
        gradeListLayout=QVBoxLayout()
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
        gradeListLayout.addLayout(titleLayout)
        self.gradeList = QTableWidget()
        self.gradeList.setRowCount(15)
        self.gradeList.setColumnCount(3)
        self.gradeList.verticalHeader().setVisible(False)
        self.gradeList.horizontalHeader().setVisible(False)
        self.gradeList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.gradeList.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.buttonList = []
        self.funcList=[]
        for i in range(15):
            button=QPushButton("显示")
            button.setDown(True)
            button.setStyleSheet('QPushButton{margin:5px}')
            button.setEnabled(False)
            self.buttonList.append(button)
            self.funcList.append(self.makeFunc(i))
            self.gradeList.setCellWidget(i,2,button)
        gradeListLayout.addWidget(self.gradeList)
        return gradeListLayout

    def visitorShow(self,visitorList):
        self.visitorList=visitorList
        #便于传参
        for index in range(15):
            self.gradeList.setItem(index,0,QTableWidgetItem(""))
            self.gradeList.setItem(index,1,QTableWidgetItem(""))
        for index in range(len(visitorList)):
            #列表显示
            self.gradeList.setItem(index,0,QTableWidgetItem(str(visitorList[index]["name"])))
            self.gradeList.setItem(index,1,QTableWidgetItem(str(visitorList[index]["time"])))
            self.buttonList[index].setEnabled(True)
            self.buttonList[index].clicked.connect(self.funcList[index])
            #不要使用lambda表达式，会延迟函数的执行，导致出错


    def makeFunc(self,index):
        def detailShow():
            studentData=self.visitorList[index]
            self.nameLable.setText(str(studentData["name"]))
            self.numLable.setText(str(studentData["num"]))
            self.classLable.setText(studentData["class"])
            self.phoneLable.setPlainText(studentData["phone"])
        return detailShow
