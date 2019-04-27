from PyQt5.QtWidgets import *
import PyQt5.QtCore
from PyQt5.QtGui import *
from window import *

class doorWindow(window):
    def __init__(self,width=1366,height=768):
        window.__init__(self,width,height)
        self.doorWindowLayout=PyQt5.QtWidgets.QVBoxLayout()
        #总布局1
        table=QTableWidget()
        #1.1列表
        table.setRowCount(4)
        table.setColumnCount(4)
        #四行四列
        table.setHorizontalHeaderLabels(['照片', '姓名', '学号','来访时间'])
        #标题字段
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #水平自由伸缩
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #竖直自由伸缩
        table.verticalHeader().setVisible(False)
        #不可编辑
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        #第一列自适应宽度
        for i in range(4):
            img=QLabel()
            per=QPixmap('per.jpg')
            img.setPixmap(per)
            table.setCellWidget(i,0,img)
        self.doorWindowLayout.addWidget(table)
        # 加入1.1
        self.setLayout(self.doorWindowLayout)
        #设置总布局
        self.showFullScreen()
        #全屏





