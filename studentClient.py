from PyQt5.QtWidgets import *
import PyQt5.QtCore
from PyQt5.QtGui import *
from window import *
from doorClient import *
class studentWindow(window):
    def __init__(self,width=1366,height=768):
        window.__init__(self,width,height)
        self.doorWindowLayout=QVBoxLayout()
        #总布局1
        self.setLayout(self.doorWindowLayout)
        # self.tabel=QTableWidget()
        # #1.1列表
        # self.tabel.setRowCount(3)
        # self.tabel.setColumnCount(1)
        # #四行四列
        # self.tabel.setHorizontalHeaderLabels(['照片', '姓名', '备注信息'])
        # #标题字段
        # self.tabel.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # #水平自由伸缩
        # self.tabel.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # #竖直自由伸缩
        # self.tabel.verticalHeader().setVisible(False)
        # #隐藏行号
        # self.tabel.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # #第一列自适应
        # for i in range(4):
        #     doorimg=QLabel()
        #     per=QPixmap('per.jpg')
        #     doorimg.setPixmap(per)
        #     self.tabel.setCellWidget(i,0,doorimg)
        # self.doorWindowLayout.addWidget(self.tabel)
        # # 加入1.1
        # self.setLayout(self.doorWindowLayout)
        # #设置总布局
        # # self.showFullScreen()
        # #全屏
    def visitorShow(self,visitorList):
        for index in range(len(visitorList)):

            nameLable=QLabel(visitorList(index)["name"])
            font=QFont("Microsoft YaHei", 20, 75)
            #字体格式
            nameLable.setFont(font)
            self.tabel.setCellWidget(index,1,nameLable)

            tiplable = QLabel(visitorList(index)["name"]+"你好，你的辅导员"+visitorList(index)["teacher"]+"正在等待为你解决问题")
            font = QFont("Microsoft YaHei", 20, 75)
            # 字体格式
            tiplable.setFont(font)
            self.tabel.setItem(index,2,tiplable)




