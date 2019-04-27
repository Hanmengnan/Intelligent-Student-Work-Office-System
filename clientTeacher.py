from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore
from window import *
class teacherWindow(window):
    def __init__(self, width=1366, height=768):
        window.__init__(self, width, height)
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
        self.showFullScreen()
        #全屏
    def gradeData(self):
        """
        右侧布局
        :return:
        """
        gradeListLayout=QVBoxLayout()
        #1.2右侧布局
        text = QLabel("科目成绩")
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
        gradeList = QTableWidget()
        #1.2.2表格
        gradeList.setRowCount(50)
        gradeList.setColumnCount(3)
        #行列数
        gradeList.setHorizontalHeaderLabels(['学期', '课程名称', '成绩'])
        #表格字段
        gradeList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        gradeList.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #水平竖直自适应延申
        gradeListLayout.addWidget(gradeList)
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
        num=QLineEdit()
        num.setReadOnly(True)
        name=QLineEdit()
        name.setReadOnly(True)
        id=QLineEdit()
        id.setReadOnly(True)
        year=QLineEdit()
        year.setReadOnly(True)
        inclass=QLineEdit()
        inclass.setReadOnly(True)
        major=QLineEdit()
        major.setReadOnly(True)
        studentDataList.addRow(numlabel,num)
        studentDataList.addRow(namelabel, name)
        studentDataList.addRow(idlabel, id)
        studentDataList.addRow(yearlabel, year)
        studentDataList.addRow(inclasslabel, inclass)
        studentDataList.addRow(majorlabel, major)


        studentDataLayoutUp.addLayout(studentDataList)
        #加入1.1.2.2
        studentDataLayout.addLayout(studentDataLayoutUp)
        #加入1.1.2

        studentDataLayoutDown = QHBoxLayout()
        # 1.1.3下方布局
        otherData=QLabel("")
        #1.1.3.1
        otherData.setAutoFillBackground(True)
        otherData.setFrameShadow(QtWidgets.QFrame.Raised)
        palettedown = QPalette()
        palettedown.setColor(QPalette.Window, Qt.white)
        otherData.setPalette(palettedown)
        #设置背景
        otherData.setFixedWidth(700)
        otherData.setFixedHeight(450)
        studentDataLayoutDown.addWidget(otherData)
        #加入1.1.3.1
        studentDataLayout.addLayout(studentDataLayoutDown)
        #加入1.1.3
        return  studentDataLayout