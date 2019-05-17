import time
from settings import *
from PyQt5.QtCore import *
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from database import *
from settings import *


class thread(QThread):
    emptySignal = pyqtSignal()
    showSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        #这东西和线程有什么区别
        sched = BlockingScheduler()
        trigger = IntervalTrigger(seconds=PERTIME)
        sched.add_job(self.getinfo, trigger)
        sched.start()

    def getinfo(self):
        response = visitor()
        if response ==[]:
            pass
        else:
            self.showSignal.emit(response)

class visitorThread(QThread):
    deleteSignal=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.mytime=DOOR_VISITOR_TIME
    def run(self):
        while True:
            time.sleep()
            if self.mytime==0:
                self.deleteSignal.emit()
            self.mytime-=1