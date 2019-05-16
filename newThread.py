import requests
from PyQt5.QtCore import *
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time
from database import *


class thread(QThread):
    emptySignal = pyqtSignal()
    showSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        #这东西和线程有什么区别
        sched = BlockingScheduler()
        trigger = IntervalTrigger(seconds=1)
        sched.add_job(self.getinfo, trigger)
        sched.start()

    def getinfo(self):
        response = visitor()
        if response ==[]:
            pass
        else:
            # response = {"name": response[0][2] , "num": response[0][1]}
            self.showSignal.emit(response)
            print("emit")

class visitorThread(QThread):
    deleteSignal=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.mytime=60
    def run(self):
        while True:
            time.sleep(1)
            if self.mytime==0:
                self.deleteSignal.emit()
            self.mytime-=1