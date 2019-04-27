from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette

from window import *
from PyQt5.QtWidgets import *
from clock import *
class studentWindow(window):
    def __init__(self):
        window.__init__(self,width=1366,height=768)

        clientStudentLayout = QVBoxLayout()
        #1总布局
        teacherDataLayout=QHBoxLayout()
        #1.1上层布局
        img = QLabel()
        #1.1.1
        per = QPixmap('per.jpg')
        img.setPixmap(per)
        teacherDataLayout.addWidget(img)
        #加入1.1.1

        teacherData=QFormLayout()
        #1.1.2
        teacherData.setSpacing(105)
        #字段间距

        palettenew = QPalette()
        palettenew.setColor(QPalette.Window, Qt.darkCyan)
        #便签背景颜色

        namelable = QLabel("教师名称：")
        namelable.setAutoFillBackground(True)
        namelable.setFixedWidth(200)
        namelable.setFrameShape(QtWidgets.QFrame.Box)
        namelable.setPalette(palettenew)
        #字段：教师名称
        tellabel = QLabel("Tel：")
        tellabel.setAutoFillBackground(True)
        tellabel.setFixedWidth(200)
        tellabel.setFrameShape(QtWidgets.QFrame.Box)
        tellabel.setPalette(palettenew)
        #字段：
        emaillabel = QLabel("E-mail：")
        emaillabel.setAutoFillBackground(True)
        emaillabel.setFixedWidth(200)
        emaillabel.setFrameShape(QtWidgets.QFrame.Box)
        emaillabel.setPalette(palettenew)
        #字段：
        tel = QLineEdit()
        tel.setReadOnly(True)
        tel.setFixedWidth(200)
        name = QLineEdit()
        name.setReadOnly(True)
        name.setFixedWidth(200)
        email = QLineEdit()
        email.setReadOnly(True)
        email.setFixedWidth(200)

        teacherData.addRow(namelable,name)
        teacherData.addRow(tellabel,tel)
        teacherData.addRow(emaillabel,email)
        #栅格布局加入控件
        teacherDataLayout.addLayout(teacherData)
        #加入1.1.2
        timer=MyTimer()
        timer.setFixedHeight(100)
        timer.setFixedWidth(400)
        teacherDataLayout.addWidget(timer)
        #加入1.1.3
        clientStudentLayout.addLayout(teacherDataLayout)
        # 加入1.1
        teacherWordLable = QLabel("""老师寄语：
        你爱惜你的生命，从不浪费时间，因为你知道：时间就是塑造生命的材料。
        祝你们好好学习！天天进步！快乐成长！""")

        teacherWordLable.setFixedWidth(1365)
        teacherWordLable.setFixedHeight(500)
        font=QFont("Microsoft YaHei", 20, 75)
        #字体格式
        teacherWordLable.setFont(font)
        #1.2下层标签
        clientStudentLayout.addWidget(teacherWordLable)
        #加入1.2
        self.setLayout(clientStudentLayout)
        #设置总布局

