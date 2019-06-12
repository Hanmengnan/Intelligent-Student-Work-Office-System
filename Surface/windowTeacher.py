import PyQt5.QtCore
import sys
from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap , QPalette
from PyQt5.QtWidgets import *
from Surface.window import *
from Surface.database import *
from PyQt5.QtCore import pyqtSignal, Qt
buttonStyle='QPushButton{background-color:rgb(0,206,209);color: white;border-radius: 18px;  border: 5px groove gray;border-style: outset;}''QPushButton:hover{background-color:rgb(175,238,238); color: black;}''QPushButton:pressed{background-color:rgb(0,191,255);border-style: inset; }'
lableStyle= 'QLabel{font-size:30px;color: white;  border: 20px groove gray;border-style: outset;}'
editStyle='QLineEdit{background-color:rgb(0,206,209);font-size:30px;color: white; border-radius: 18px; border: 20px groove gray;border-style: outset;}'
comboBoxStyle="QComboBox{background-color:rgb(0,206,209);font-family:'微软雅黑';font-size:15; border:1px solid lightgray;}"
class teacherWindow(window):
    control_signal= pyqtSignal(list)
    buttonList = []
    funcList = []
    visitorList=[]
    def __init__(self, width=2160, height=1440):
        window.__init__(self, width, height)
        wholepalette = QPalette()
        wholepalette.setColor(QPalette.Window, QColor(1, 28, 52))
        self.setPalette(wholepalette)
        #背景颜色
        wholeLayout=QHBoxLayout()
        #整体布局
        studentDataLayout=QVBoxLayout()
        #左侧布局
        img = self.studentImgGround()
        #头像区域
        studentDataLayout.addWidget(img)
        self.data=self.studentDataGround()
        #详细信息区域
        studentDataLayout.addWidget(self.data)

        wholeLayout.addLayout(studentDataLayout)

        visitorData = self.tableGround()
        #表格区域
        visitorRecord = QWidget()
        visitorRecord.setStyleSheet("QWidget{border-image:url(./teacherimg/STARS.png);}")
        visitorRecord.setLayout(visitorData)
        wholeLayout.addWidget(visitorRecord)
        self.setLayout(wholeLayout)
        self.write()
        self.showFullScreen()
        self.mainPageShow()

    def studentImgGround(self):
        background = QWidget()
        background.setFixedHeight(850)
        background.setFixedWidth(1000)
        background.setStyleSheet('QWidget{border-image:url(./teacherimg/头像区域.png);}')
        perimgLayout = QVBoxLayout()
        perimgLayout.setAlignment(Qt.AlignHCenter)
        self.perimg = QWidget()
        self.perimg.setFixedHeight(500)
        self.perimg.setFixedWidth(400)
        self.perimg.setStyleSheet("QWidget{border-image:url(./teacherimg/头像.png);}")
        perimgLayout.setAlignment(QtCore.Qt.AlignCenter)
        perimgLayout.addWidget(self.perimg)
        background.setLayout(perimgLayout)
        return background

    def studentDataGround(self):
        def wordSet(lable):
            lable.setMaximumHeight(50)
            lable.setFont(QFont("微软雅黑", 17, QFont.Bold))
            lable.setStyleSheet('color:rgb(207, 214, 218)')

        self.data = QWidget()
        self.data.setFixedWidth(1000)
        self.data.setFixedHeight(530)
        self.data.setAutoFillBackground(True)

        datapalette = QPalette()
        datapalette.setBrush(QPalette.Background, QBrush(QPixmap("./teacherimg/信息底图.png")))
        self.data.setPalette(datapalette)

        dataBackgroundLayout=QGridLayout()

        empty = QLabel("")
        wordSet(empty)
        empty.setFixedWidth(150)
        dataBackgroundLayout.addWidget(empty , 0 ,0 , 1 ,1 )

        self.nameLable=QLabel("")
        wordSet(self.nameLable)
        dataBackgroundLayout.addWidget(self.nameLable,1,1,1,3)

        empty = QLabel("")
        empty.setFixedWidth(130)
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

        return self.data






    def tableGround(self):

        tableGround=QVBoxLayout()
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
        #tableGround.addLayout(titleLayout)

        self.table = QTableWidget(12, 4)
        self.table.setStyleSheet("QTableWidget::item{border:2px solid ; border-color: rgb(39,64,139);font-size:12px}")
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 自适应宽度
        for i in range(12):
            button_tempLayout = QVBoxLayout()
            button_tempWidget = QWidget()
            button_tempLayout.setAlignment(Qt.AlignCenter)
            button = QPushButton("显示")
            # button.setDown(False)
            button.setFixedWidth(200)
            button.setFixedHeight(80)
            button.setStyleSheet(buttonStyle)
            # button.setEnabled(False)
            self.buttonList.append(button)
            self.funcList.append(self.makeFunc(i))
            button_tempLayout.addWidget(button)
            button_tempWidget.setLayout(button_tempLayout)
            self.table.setCellWidget(i, 3, button_tempWidget)
            self.buttonList[i].clicked.connect(self.funcList[i])

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layoutBanner = QHBoxLayout()
        tipLable=QLabel("当前页数")
        # tipLable.setFixedWidth(180)
        tipLable.setStyleSheet(lableStyle)
        self.curPage=QLabel("1")
        self.curPage.setFixedWidth(60)
        self.curPage.setStyleSheet(lableStyle)
        self.loginBox=self.loginWindow()
        self.prevButton = QPushButton("前一页")
        self.prevButton.setFixedHeight(55)
        self.prevButton.setFixedWidth(180)
        self.prevButton.setStyleSheet(buttonStyle)
        self.prevButton.clicked.connect(self.__pre_page)
        self.backButton = QPushButton("后一页")
        self.backButton.setFixedHeight(55)
        self.backButton.setFixedWidth(180)
        self.backButton.clicked.connect(self.__next_page)
        self.backButton.setStyleSheet(buttonStyle)
        layoutBanner.addWidget(tipLable)

        layoutBanner.addWidget(self.curPage)
        layoutBanner.addWidget(self.loginBox)
        layoutBanner.addWidget(self.prevButton)
        layoutBanner.addWidget(self.backButton)
        widget = QWidget()
        widget.setLayout(layoutBanner)
        layout.addWidget(widget)
        self.control_signal.connect(self.page_controller)
        tableGround.addLayout(layout)
        return tableGround

    def loginWindow(self):
        widget=QWidget()
        layout = QHBoxLayout()
        self.box = QComboBox()
        self.box.setFixedHeight(55)
        self.box.setFixedWidth(180)
        self.box.setStyleSheet(comboBoxStyle)
        self.box.addItems(["全部", "2015", "2016", "2017", "2018"])
        button = QPushButton("确认")
        button.setFixedHeight(60)
        button.setFixedWidth(180)
        button.setStyleSheet(buttonStyle)
        button.clicked.connect(self.write)
        layout.addWidget(self.box)
        layout.addWidget(button)
        widget.setLayout(layout)
        return widget

    def write(self):
        g=self.box.currentText()
        f=open("./grade.txt","w")
        f.write(g)
        f.close()
        self.mainPageShow()
        self.curPage.setText("1")

    def __pre_page(self):
        """点击上一页信号"""
        self.control_signal.emit(["pre", self.curPage.text()])

    def __next_page(self):
        """点击下一页信号"""

        self.control_signal.emit(["next", self.curPage.text()])


    def page_controller(self, signal):
        total_page = self.getPageCount()
        self.index=int(signal[1])
        print(self.index)
        if "home" == signal[0]:
            self.curPage.setText("1")
        elif "pre" == signal[0]:
            if 1 == int(signal[1]):
                return
            self.curPage.setText(str(self.index - 1))
            print(self.index)
        elif "next" == signal[0]:
            if total_page == int(signal[1]):
                return
            self.curPage.setText(str(self.index + 1))
        self.visitorShow(int(self.curPage.text()))  # 改变表格内容

    def getPageCount(self):
        return (dataCount()+11)/12
    def mainPageShow(self):
        try:
            if self.curPage.text()=="1":
                self.visitorShow(1)
        except:
            pass
    def visitorShow(self,pageindex):
        visitorList=change_page(pageindex)
        print(visitorList)
        #便于传参
        for index in range(12):
            self.table.setItem(index,0,QTableWidgetItem(""))
            self.table.setItem(index,1,QTableWidgetItem(""))
        font=QFont()
        font.setPointSize(12)
        for index in range(len(visitorList)):
            #列表显示
            id = QTableWidgetItem(str(visitorList[index][1]))
            id.setTextAlignment(Qt.AlignCenter)
            id.setFont(font)
            id.setForeground(QBrush(QColor(255, 255, 255)))
            self.table.setItem(index, 0,id )
            name=QTableWidgetItem(str(visitorList[index][2]))
            name.setTextAlignment(Qt.AlignCenter)
            name.setFont(font)
            name.setForeground(QBrush(QColor(255 ,255 ,255 )))
            self.table.setItem(index,1,name)
            num = QTableWidgetItem(visitorList[index][4].strftime("%Y-%m-%d %H:%M:%S"))
            num.setTextAlignment(Qt.AlignCenter)
            num.setFont(font)
            num.setForeground(QBrush(QColor(255 , 255 , 255)))
            self.table.setItem(index,2,num)

            #不要使用lambda表达式，会延迟函数的执行，导致出错
    def makeFunc(self,index):
        def detailShow():
            if (self.table.item(index,0)!=None):
                id=self.table.item(index,0).text()
                data=detail(id)
                if data!=[]:
                    self.nameLable.setText(data["xm"])
                    self.classLable.setText(data["bj"])
                    self.phonenumber.setText(data["dh"])
                    self.idnumber.setText(data["xh"])
                    self.parentphonenumber.setText(data["jzdh"])
                    self.province.setText(data["jg"])
                    self.address.setText(data["dz"])

        return detailShow




