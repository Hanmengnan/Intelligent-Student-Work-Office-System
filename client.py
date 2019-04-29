import newThread
from clientTeacher import *
import sys
class client:


    def showInfo(self,response):
        data=[]
        response=str(response)[1:-1].split('(').split(',')
        for i in response:
            if response.index(i) != 0:
                num=int(i.split(',')[1][2:-2])
                name=i.split(',')[2][1:-1]
                data.append({"name":name,"num":num})
        #response=str(response).replace('(','').replace(')','').replace('\'','').split(',')
        # data=[{"name":response[0][2],"num":response[0][1]}]
        #data=[{"name":response[2],"num":response[1]}]
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



