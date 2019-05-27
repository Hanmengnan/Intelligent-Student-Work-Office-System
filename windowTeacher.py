import PyQt5.QtCore
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap , QPalette
from PyQt5.QtWidgets import *
from window import *
from database import tableVisitor
class perimg(QWidget):
    def __init__(self):
        QWidget.__init__(self)
    def newWidget(self):
        background=QWidget()
        background.setFixedHeight(1000)
        background.setFixedWidth(1200)
        background.setStyleSheet('QWidget{border-image:url(./teacherimg/头像区域.png);}')
        perimgLayout = QVBoxLayout()
        perimgLayout.setAlignment(Qt.AlignHCenter)
        perimg = QWidget()
        perimg.setFixedHeight(600)
        perimg.setFixedWidth(500)
        perimg.setStyleSheet("QWidget{border-image:url(./teacherimg/头像.png);}")
        perimgLayout.setAlignment(QtCore.Qt.AlignCenter)
        perimgLayout.addWidget(perimg)
        background.setLayout(perimgLayout)
        return background

class teacherWindow(window):
    buttonList = []
    funcList = []
    visitorList=[]
    def __init__(self, width=2736, height=1824):
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
        self.data.setFixedWidth(1400)
        self.data.setFixedHeight(800)

        self.data.setAutoFillBackground(True)

        datapalette = QPalette()
        datapalette.setBrush(QPalette.Background, QBrush(QPixmap("./teacherimg/信息底图.png")))
        self.data.setPalette(datapalette)

        dataBackgroundLayout=QGridLayout()
        def wordSet(lable):
            lable.setMaximumHeight(50)
            lable.setFont(QFont("微软雅黑", 19, QFont.Bold))
            lable.setStyleSheet('color:rgb(207, 214, 218)')

        empty = QLabel("")
        wordSet(empty)
        empty.setFixedWidth(200)
        dataBackgroundLayout.addWidget(empty , 0 ,0 , 1 ,1 )

        self.nameLable=QLabel("")
        wordSet(self.nameLable)
        dataBackgroundLayout.addWidget(self.nameLable,1,1,1,3)

        empty = QLabel("")
        empty.setFixedWidth(220)
        dataBackgroundLayout.addWidget(empty , 1 , 4 , 1 , 1)

        self.classLable = QLabel("")
        wordSet(self.classLable)
        dataBackgroundLayout.addWidget(self.classLable , 1 , 5 , 1 , 2)

        self.idnumber = QLabel("")
        wordSet(self.idnumber)
        dataBackgroundLayout.addWidget(self.idnumber,2,1,1,3)

        self.score = QLabel("")
        wordSet(self.score)
        dataBackgroundLayout.addWidget(self.score , 2 , 5 , 1 , 2)

        self.phonenumber = QLabel("")
        wordSet(self.phonenumber)
        dataBackgroundLayout.addWidget(self.phonenumber , 3, 1 , 1 , 3)

        empty = QLabel("")
        dataBackgroundLayout.addWidget(empty , 3 , 5 , 1 , 1)

        self.parentphonenumber = QLabel("")
        self.parentphonenumber.setMaximumHeight(80)
        wordSet(self.parentphonenumber)
        dataBackgroundLayout.addWidget(self.parentphonenumber , 3 , 6 , 1 , 3)

        self.province = QLabel("")
        wordSet(self.province)
        dataBackgroundLayout.addWidget(self.province , 4 , 2 , 1 , 2)

        self.party = QLabel("")
        self.party.setMaximumHeight(80)
        wordSet(self.party)
        dataBackgroundLayout.addWidget(self.party , 4 , 6 , 1 , 3)


        self.address = QLabel("")
        wordSet(self.address)
        dataBackgroundLayout.addWidget(self.address , 5 , 2, 1 , 7)

        self.other = QLabel("")
        wordSet(self.other)
        dataBackgroundLayout.addWidget(self.other , 6 , 2 , 1 , 7)

        self.data.setLayout(dataBackgroundLayout)

        studentDataLayout.addWidget(self.data)

        wholeLayout.addLayout(studentDataLayout)

        visitorData=self.gradeData()
        visitorRecord = QWidget()
        visitorRecord.setStyleSheet("QWidget{border-image:url(./teacherimg/STARS.png);}")
        visitorRecord.setLayout(visitorData)

        wholeLayout.addWidget(visitorRecord)

        self.setLayout(wholeLayout)
        self.showFullScreen()



    def gradeData(self):

        visitorListLayout=QVBoxLayout()
        titleLayout = QGridLayout()
        visitor = QLabel()
        img = PyQt5.QtGui.QPixmap('./teacherimg/访客记录.png')
        visitor.setPixmap(img)
        titleLayout.addWidget(visitor , 0 , 1)
        name = QLabel()
        name.setFixedWidth(500)
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
        self.visitorTableWidge.setEnabled(False)
        self.visitorTableWidge.setRowCount(12)
        self.visitorTableWidge.setColumnCount(3)
        self.visitorTableWidge.setStyleSheet("QTableWidget::item{border:2px solid ; border-color: rgb(39,64,139);font-size:12px}")
        self.visitorTableWidge.verticalHeader().setVisible(False)
        self.visitorTableWidge.horizontalHeader().setVisible(False)
        self.visitorTableWidge.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.visitorTableWidge.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)



        for i in range(12):
            button_tempLayout=QVBoxLayout()
            button_tempWidget=QWidget()
            button_tempLayout.setAlignment(Qt.AlignCenter)
            button=QPushButton("显示")
            button.setDown(True)
            button.setFixedWidth(200)
            button.setFixedHeight(80)
            button.setStyleSheet('QPushButton{background-color:rgb(0,206,209);color: white;border-radius: 18px;  border: 20px groove gray;border-style: outset;}'
                                   'QPushButton:hover{background-color:rgb(175,238,238); color: black;}'
                                   'QPushButton:pressed{background-color:rgb(0,191,255);border-style: inset; }')
            button.setEnabled(False)
            self.buttonList.append(button)
            self.funcList.append(self.makeFunc(i))
            button_tempLayout.addWidget(button)
            button_tempWidget.setLayout(button_tempLayout)
            self.visitorTableWidge.setCellWidget(i,2,button_tempWidget)
        visitorListLayout.addWidget(self.visitorTableWidge)
        return visitorListLayout



    def tableListShow(self):
        self.visitorList=tableVisitor()
        self.visitorTableWidge

    def visitorShow(self,visitorList):
        self.visitorList=self.visitorList+visitorList
        #便于传参
        for index in range(12):
            self.visitorTableWidge.setItem(index,0,QTableWidgetItem(""))
            self.visitorTableWidge.setItem(index,1,QTableWidgetItem(""))

        for index in range(len(self.visitorList)):
            #列表显示
            name=QTableWidgetItem(str(self.visitorList[index]["xm"]))
            name.setForeground(QBrush(QColor(255 ,255 ,255 )))
            self.visitorTableWidge.setItem(index,0,name)

            num = QTableWidgetItem(str(self.visitorList[index]["time"]))
            num.setForeground(QBrush(QColor(255 , 255 , 255)))
            self.visitorTableWidge.setItem(index,1,num)

            self.buttonList[index].setEnabled(True)
            self.buttonList[index].clicked.connect(self.funcList[index])
            #不要使用lambda表达式，会延迟函数的执行，导致出错


    def makeFunc(self,index):
        def detailShow():
            if (self.visitorTableWidge.item(index,0)!=None):
                name=self.visitorTableWidge.item(index,0).text()
                detailShow(name)
            # studentData=self.visitorList[index]
            # self.nameLable.setText(str(studentData["xm"]))
            # self.idnumber.setText(str(studentData["xh"]))
            # self.classLable.setText(studentData["bj"])
            # self.phonenumber.setText(studentData["dh"])
            # self.parentphonenumber.setText(studentData["jzdh"])
            # self.province.setText(studentData["jg"])
            # self.address.setText(studentData["dz"])


        return detailShow
    def visitorDelete(self):
        for index in range(12):
            self.visitorTableWidge.setItem(index , 0 , QTableWidgetItem(""))
            self.visitorTableWidge.setItem(index , 1 , QTableWidgetItem(""))
        self.nameLable.setText("")
        self.idnumber.setText("")
        self.classLable.setText("")
        self.phonenumber.setText("")
        self.parentphonenumber.setText("")
        self.province.setText("")
        self.address.setText("")