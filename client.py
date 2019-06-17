from Door.windowDoor import doorWindow
from newThread import *
from windowTeacher import *
import sys
#from Door.windowDoor import *
class doorClient:
    data=[]
    def showInfo(self,response):
        self.visitorthread.mytime=60
        self.data = response + self.data
        if len(self.data)>3:
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
        self.mywindow.mainPageShow()
        self.mywindow.first_show()
    def do(self):
        amywindow = QApplication(sys.argv)
        self.mywindow = teacherWindow()
        self.mywindow.show()
        massagethread = thread()
        massagethread.start()
        massagethread.showSignal.connect(self.showInfo)

        sys.exit(amywindow.exec_())

