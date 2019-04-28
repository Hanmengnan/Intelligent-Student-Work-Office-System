import newThread
from clientTeacher import *
import sys
class client:


    def showInfo(self,response):
        response=str(response).replace('(','').replace(')','').replace('\'','').split(',')
        # data=[{"name":response[0][2],"num":response[0][1]}]
        data=[{"name":response[2],"num":response[1]}]
        print(data)
        self.pp.visitorShow(data)

    def do(self):
        app = QApplication(sys.argv)
        self.pp = teacherWindow()
        self.pp.show()
        t=newThread.thread()
        t.start()
        t.showSignal.connect(self.showInfo)
        sys.exit(app.exec_())



