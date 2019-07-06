import Door.windowDoor
from newThread import *

import sys

from teacherContorl import *

class doorClient:
    """
    门口端,数据分发类
    """
    data=[]#访客列表
    def ShowInfo(self,response):
        """
        显示函数
        :param response:
        :return:
        """
        self.visitorthread.mytime=60#倒计时时间
        self.data = response + self.data
        if len(self.data)>3:#界面最多显示三个来访者
            self.data.pop(-1)#删除最早的来访者
        self.mywindow.visitorShow(self.data)

    def ResetWindow(self):
        """
        倒计时结束，界面清空函数
        :return:
        """
        self.mywindow.visitorDelete()#界面清空
        self.data=[]#列表置空

    def do(self):
        """
        启动
        :return:
        """
        app = QApplication(sys.argv)

        self.DoorWindow = Door.windowDoor.doorWindow()
        self.DoorWindow.show()

        MyThread=usualThread()
        MyThread.start()
        MyThread.showSignal.connect(self.ShowInfo)

        DeleteThread = deleteThread()
        DeleteThread.start()
        DeleteThread.deleteSignal.connect(self.ResetWindow)

        sys.exit(app.exec_())




class teacherClient(doorClient):
    """
    教师端，数据分发类
    """
    def ShowInfo(self):
        """
        显示
        :return:
        """
        self.ClientWindow.MainPageShow()
    def do(self):
        """
        启动
        :return:
        """
        app = QApplication(sys.argv)

        self.ClientWindow = teacherControl()
        self.ClientWindow.show()

        MyThread = usualThread()
        MyThread.start()

        MyThread.showSignal.connect(self.ShowInfo)
        sys.exit(app.exec_())

