from newThread import *
from clientTeacher import *
import sys
from doorClient import *
class client:
    data=[]
    def showInfo(self,response):
        try:
            self.visitorthread.mytime=180
            response=response[1:-1].split(',')
            for i in range(1,151,10):
                num=int(response[i][2:-1])
                name=response[i+1][2:-1]
                self.data.append({"name":name,"num":num})
                self.data.reverse()
        except:
            pass
        self.pp.visitorShow(self.data)

    def deleteVisitor(self):
        self.data=[]

    def do(self):
        app = QApplication(sys.argv)
        self.pp = teacherWindow()
        self.pp.show()
        massagethread=thread()
        massagethread.start()
        massagethread.showSignal.connect(self.showInfo)
        self.visitorthread = visitorThread()
        self.visitorthread.start()
        self.visitorthread.deleteSignal.connect(self.deleteVisitor)
        sys.exit(app.exec_())



