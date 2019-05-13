import requests
from PyQt5.QtCore import *
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import time


class thread(QThread):
    emptySignal = pyqtSignal()
    showSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
    def run(self):
        sched = BlockingScheduler()
        trigger = IntervalTrigger(seconds=1)
        sched.add_job(self.getinfo, trigger)
        sched.start()

    def getinfo(self):
        response = requests.get('http://10.5.102.59:5000').text
        if response == "()":
            pass
        else:
            print(response)
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