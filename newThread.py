import requests
from PyQt5.QtCore import *
from apscheduler.schedulers.blocking import BlockingScheduler


class thread(QThread):
    emptySignal = pyqtSignal()
    showSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        sched = BlockingScheduler()
        sched.add_job(self.getinfo, 'interval', seconds=1)
        sched.start()

    def getinfo(self):
        response = requests.get('http://192.168.1.100:5000').text
        print(response)
        if response == "()":
            pass
        else:
            self.showSignal.emit(response)
