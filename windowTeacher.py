import PyQt5.QtCore
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap , QPalette
from PyQt5.QtWidgets import *
from window import *

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
        #背景颜色
        wholeLayout=QHBoxLayout()

        studentDataLayout=QVBoxLayout()

        background = perimg().newWidget()

        studentDataLayout.addWidget(background)

        self.data = QWidget()
        self.data.setFixedWidth(700)
        self.data.setFixedHeight(400)

        self.data.setAutoFillBackground(True)

        datapalette = QPalette()
        datapalette.setBrush(QPalette.Background, QBrush(QPixmap("./teacherimg/信息底图.png")))
        self.data.setPalette(datapalette)

        dataBackgroundLayout=QGridLayout()

        def wordSet(lable):
            lable.setFont(QFont("微软雅黑", 17, QFont.Bold))
            lable.setStyleSheet('color:rgb(207, 214, 218)')

        empty = QLabel("")
        wordSet(empty)
        empty.setFixedWidth(100)
        dataBackgroundLayout.addWidget(empty , 0 ,0 , 1 ,1 )

        self.nameLable=QLabel("韩孟男")
        wordSet(self.nameLable)
        dataBackgroundLayout.addWidget(self.nameLable,1,1,1,3)

        empty = QLabel("")
        empty.setFixedWidth(100)
        dataBackgroundLayout.addWidget(empty , 1 , 4 , 1 , 1)

        self.classLable = QLabel("计17-3")
        wordSet(self.classLable)
        dataBackgroundLayout.addWidget(self.classLable , 1 , 5 , 1 , 2)

        self.idnumber = QLabel("17159010325")
        wordSet(self.idnumber)
        dataBackgroundLayout.addWidget(self.idnumber,2,1,1,3)

        self.score = QLabel("88.67")
        wordSet(self.score)
        dataBackgroundLayout.addWidget(self.score , 2 , 5 , 1 , 2)

        self.phonenumber = QLabel("15042098397")
        wordSet(self.phonenumber)
        dataBackgroundLayout.addWidget(self.phonenumber , 3, 1 , 1 , 3)

        empty = QLabel("")
        empty.setFixedWidth(40)
        dataBackgroundLayout.addWidget(empty , 3 , 5 , 1 , 1)

        self.parentphonenumber = QLabel("15042098397")
        wordSet(self.parentphonenumber)
        dataBackgroundLayout.addWidget(self.parentphonenumber , 3 , 6 , 1 , 3)

        self.province = QLabel("内蒙古")
        wordSet(self.province)
        dataBackgroundLayout.addWidget(self.province , 4 , 2 , 1 , 2)

        self.party = QLabel("共青团员")
        wordSet(self.party)
        dataBackgroundLayout.addWidget(self.party , 4 , 6 , 1 , 3)


        self.address = QLabel("***********")
        wordSet(self.address)
        dataBackgroundLayout.addWidget(self.address , 5 , 2, 1 , 7)

        self.other = QLabel("***********")
        wordSet(self.other)
        dataBackgroundLayout.addWidget(self.other , 6 , 2 , 1 , 7)

        self.data.setLayout(dataBackgroundLayout)

        studentDataLayout.addWidget(self.data)

        wholeLayout.addLayout(studentDataLayout)

        tempLable = QLabel()
        img = PyQt5.QtGui.QPixmap('./teacherimg/分隔.png')
        tempLable.setPixmap(img)
        wholeLayout.addWidget(tempLable)

        visitorData=self.gradeData()
        visitorRecord = QWidget()
        visitorRecord.setStyleSheet("QWidget{border-image:url(./teacherimg/STARS.png);}")
        visitorRecord.setLayout(visitorData)

        wholeLayout.addWidget(visitorRecord)

        self.setLayout(wholeLayout)





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
        self.visitorTableWidge.setRowCount(15)
        self.visitorTableWidge.setColumnCount(3)
        self.visitorTableWidge.verticalHeader().setVisible(False)
        self.visitorTableWidge.horizontalHeader().setVisible(False)
        self.visitorTableWidge.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.visitorTableWidge.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.buttonList = []
        self.funcList=[]

        for i in range(15):
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
        for index in range(15):
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
        for index in range(15):
            self.visitorTableWidge.setItem(index , 0 , QTableWidgetItem(""))
            self.visitorTableWidge.setItem(index , 1 , QTableWidgetItem(""))