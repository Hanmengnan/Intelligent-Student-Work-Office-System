import PyQt5.QtCore
import  time
from database import *


class usualThread(PyQt5.QtCore.QThread):
    """
    通用线程，不断查询数据库的最新数据
    """
    showSignal = PyQt5.QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        """
        定时任务
        :return:
        """
        while True:
            try:
                self.getinfo()
            except:
                pass
            time.sleep(DOOR_CLIENT_SCHEDLUER_TIME)
    def getinfo(self):
        """
        检测是否有新的访客
        :return:
        """
        response = NewestVisitor()
        if response !=[]:
            print(response)
            UpdateLocalRecord(response)
            self.showSignal.emit(response)


class deleteThread(PyQt5.QtCore.QThread):
    """
    清空界面线程
    """
    deleteSignal=PyQt5.QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.mytime=DOOR_CLIENT_DELETE_TIME
    def run(self):
        """
        倒数60秒，时间为0时，清空界面
        :return:
        """
        while True:
            time.sleep(1)
            if self.mytime==0:
                self.deleteSignal.emit()
            self.mytime-=1