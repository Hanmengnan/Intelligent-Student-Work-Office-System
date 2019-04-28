from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import *

import window


class teacherWindow(window.window):
    def __init__(self, width=1366, height=768):
        window.window.__init__(self, width, height)
        clientTeacherLayout=QHBoxLayout()
        #1总布局
        studentDataLayout=self.studentData()
        #1.1左侧布局
        clientTeacherLayout.addLayout(studentDataLayout)
        #加入1.1
        gradeData=self.gradeData()
        #1.2右侧布局（表格）
        clientTeacherLayout.addLayout(gradeData)
        #加入1.2
        self.setLayout(clientTeacherLayout)
        #设置总布局
        # self.showFullScreen()
        #全屏
    def gradeData(self):
        """
        右侧布局
        :return:
        """
        gradeListLayout=QVBoxLayout()
        #1.2右侧布局
        text = QLabel("学生列表")
        # 1.2.1右侧布局标题
        text.setAlignment(Qt.AlignCenter)
        # 文字居中
        text.setAutoFillBackground(True)
        # 实例化
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.darkGray)
        text.setPalette(palette)
        # 设置背景
        gradeListLayout.addWidget(text)
        #加入1.2.1
        self.gradeList = QTableWidget()
        #1.2.2表格
        self.buttonList=[]
        self.gradeList.setRowCount(15)
        self.gradeList.setColumnCount(3)
        #行列数
        self.gradeList.setHorizontalHeaderLabels(['班级', '姓名',"详细信息"])
        #表格字段
        self.gradeList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.gradeList.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(15):
            button=QPushButton("显示")
            button.setDown(True)
            button.setStyleSheet('QPushButton{margin:5px}')
            button.setEnabled(False)
            self.buttonList.append(button)
            # button.setFixedHeight(30)
            # button.setFixedWidth(90)
            self.gradeList.setCellWidget(i,2,button)
        #水平竖直自适应延申
        gradeListLayout.addWidget(self.gradeList)
        #加入1.2.2
        return gradeListLayout
    def studentData(self):
        """
        左侧布局
        :return:
        """
        studentDataLayout = QVBoxLayout()
        #1.1左侧布局
        text = QLabel("个人信息")
        # 1.1.1左侧标题
        text.setAlignment(Qt.AlignCenter)
        # 文字居中
        text.setAutoFillBackground(True)
        # 实例化
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.darkGray)
        text.setPalette(palette)
        # 设置背景
        text.setFixedHeight(15)
        studentDataLayout.addWidget(text)
        #加入1.1.1
        studentDataLayoutUp = QHBoxLayout()
        #1.1.2上方布局


        img = QLabel()
        #1.1.2.1学生照片
        per = QPixmap('per.jpg')
        img.setPixmap(per)
        studentDataLayoutUp.addWidget(img)
        studentDataLayoutUp.addStretch()

        studentDataList = QFormLayout()
        #1.1.2.2学生信息布局
        studentDataList.setSpacing(28)
        #字段间距
        palettenew = QPalette()
        palettenew.setColor(QPalette.Window, Qt.darkCyan)
        #背景
        numlabel = QLabel("学号：")
        numlabel.setAutoFillBackground(True)
        numlabel.setFixedWidth(200)
        numlabel.setFrameShape(QtWidgets.QFrame.Box)
        numlabel.setPalette(palettenew)
        namelabel = QLabel("姓名：")
        namelabel.setAutoFillBackground(True)
        namelabel.setFixedWidth(200)
        namelabel.setFrameShape(QtWidgets.QFrame.Box)
        namelabel.setPalette(palettenew)
        idlabel = QLabel("身份证号：")
        idlabel.setAutoFillBackground(True)
        idlabel.setFixedWidth(200)
        idlabel.setFrameShape(QtWidgets.QFrame.Box)
        idlabel.setPalette(palettenew)
        yearlabel = QLabel("入学年份：")
        yearlabel.setAutoFillBackground(True)
        yearlabel.setFixedWidth(200)
        yearlabel.setFrameShape(QtWidgets.QFrame.Box)
        yearlabel.setPalette(palettenew)
        inclasslabel = QLabel("班级：")
        inclasslabel.setAutoFillBackground(True)
        inclasslabel.setFixedWidth(200)
        inclasslabel.setFrameShape(QtWidgets.QFrame.Box)
        inclasslabel.setPalette(palettenew)
        majorlabel = QLabel("专业：")
        majorlabel.setAutoFillBackground(True)
        majorlabel.setFixedWidth(200)
        majorlabel.setFrameShape(QtWidgets.QFrame.Box)
        majorlabel.setPalette(palettenew)
        self.num=QLineEdit()
        self.num.setReadOnly(True)
        self.name=QLineEdit()
        self.name.setReadOnly(True)
        self.id=QLineEdit()
        self.id.setReadOnly(True)
        self.year=QLineEdit()
        self.year.setReadOnly(True)
        self.inclass=QLineEdit()
        self.inclass.setReadOnly(True)
        self.major=QLineEdit()
        self.major.setReadOnly(True)
        studentDataList.addRow(numlabel,self.num)
        studentDataList.addRow(namelabel, self.name)
        studentDataList.addRow(idlabel, self.id)
        studentDataList.addRow(yearlabel, self.year)
        studentDataList.addRow(inclasslabel, self.inclass)
        studentDataList.addRow(majorlabel, self.major)


        studentDataLayoutUp.addLayout(studentDataList)
        #加入1.1.2.2
        studentDataLayout.addLayout(studentDataLayoutUp)
        #加入1.1.2

        studentDataLayoutDown = QHBoxLayout()
        # 1.1.3下方布局
        self.otherData=QTableWidget()
        #1.1.3.1
        self.otherData.setRowCount(8)
        self.otherData.setColumnCount(1)
        # 行列数
        self.otherData.setVerticalHeaderLabels(['原学院', '地区', '宿舍楼','宿舍号','性质','手机号','家长电话','家庭住址'])
        # 表格字段
        self.otherData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.otherData.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 水平竖直自适应延申
        self.otherData.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #竖直滚动条
        self.otherData.horizontalHeader().setVisible(False)
        # 隐藏列号
        studentDataLayoutDown.addWidget(self.otherData)
        #加入1.1.3.1
        studentDataLayout.addLayout(studentDataLayoutDown)
        #加入1.1.3

        return  studentDataLayout



    def visitorShow(self,visitorList):
        for index in range(len(visitorList)):
            self.gradeList.setItem(index,0,QTableWidgetItem(visitorList[index]["num"]))
            self.gradeList.setItem(index,1,QTableWidgetItem(visitorList[index]["name"]))
            self.buttonList[index].setEnabled(True)
        self.buttonList[0].clicked.connect(lambda :self.detailShow(visitorList[0]))
        self.buttonList[1].clicked.connect(lambda :self.detailShow(visitorList[1]))



    def detailShow(self,studentData):
        self.name.setText(str(studentData["name"]))
        self.num.setText(str(studentData["num"]))
        #self.inclass.setText(studentData["inclass"])
        # self.major.setPlainText(studentData["major"])
        # self.year.setPlainText(studentData["year"])
        # self.id.setPlainText(studentData["id"])
        # self.otherData.setItem(0,0,studentData[""])