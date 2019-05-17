from newThread import *
from windowTeacher import *
import sys
from windowDoor import *
from settings import *
class doorClient:
    data=[]
    def showInfo(self,response):
        self.visitorthread.mytime=DOOR_VISITOR_TIME
        self.data = response + self.data
        if len(self.data)>DOOR_VISITOR_ITEM:
            self.data.pop(-1)
        self.mywindow.visitorShow(self.data)

    def deleteVisitor(self):
        self.mywindow.visitorDelete()
        self.data=[]

    def do(self):
        amywindow = QApplication(sys.argv)
        self.mywindow = doorWindow()
        self.mywindow.show()
        massagethread=thread()
        massagethread.start()
        massagethread.showSignal.connect(self.showInfo)
        self.visitorthread = visitorThread()
        self.visitorthread.start()
        self.visitorthread.deleteSignal.connect(self.deleteVisitor)
        sys.exit(amywindow.exec_())


class teacherClient(doorClient):
    def showInfo(self,response):
        self.visitorthread.mytime = TEACHER_VISITOR_TIME
        print(self.data)
        self.data = response + self.data
        if len(self.data) > TEACHER_VISITOR_ITEM:
            self.data.pop(-1)
        self.mywindow.visitorShow(self.data)
    def do(self):
        amywindow = QApplication(sys.argv)
        self.mywindow = teacherWindow()
        self.mywindow.show()
        massagethread = thread()
        massagethread.start()
        massagethread.showSignal.connect(self.showInfo)
        self.visitorthread = visitorThread()
        self.visitorthread.start()
        self.visitorthread.deleteSignal.connect(self.deleteVisitor)
        sys.exit(amywindow.exec_())

