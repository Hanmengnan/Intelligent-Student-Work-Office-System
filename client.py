from newThread import *
from clientTeacher import *
import sys
from doorClient import *
class client:
    data=[]
    def showInfo(self,response):
        self.visitorthread.mytime=60
        response=response[1:-1].split(',')
        try:
            for i in range(1,151,10):
                num=int(response[i][2:-1])
                name=response[i+1][2:-1]
        except:
            pass
        print(self.data)
        self.data=[{"name":name,"num":num}]+self.data
        if len(self.data)>3:
            self.data.pop(3)
        
        self.pp.visitorShow(self.data)

    def deleteVisitor(self):
        self.pp.visitorDelete()
        self.data=[]

    def do(self):
        app = QApplication(sys.argv)
        self.pp = doorWindow()
        self.pp.show()
        massagethread=thread()
        massagethread.start()
        massagethread.showSignal.connect(self.showInfo)
        self.visitorthread = visitorThread()
        self.visitorthread.start()
        self.visitorthread.deleteSignal.connect(self.deleteVisitor)
        sys.exit(app.exec_())



