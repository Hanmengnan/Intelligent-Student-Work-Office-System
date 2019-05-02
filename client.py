import newThread
from clientTeacher import *
import sys
class client:


    def showInfo(self,response):
        data=[]
        try:
            """
            不要问我为什么代码如此垃圾，去问数据库工程师
            """
            response=response[1:-1].split(',')
            for i in range(1,151,10):
                num=int(response[i][2:-2])
                name=response[i+1][2:-1]
                data.append({"name":name,"num":num})
        except:
            pass
        #response=str(response).replace('(','').replace(')','').replace('\'','').split(',')
        # data=[{"name":response[0][2],"num":response[0][1]}]
        #data=[{"name":response[2],"num":response[1]}]
        self.pp.visitorShow(data)

    def do(self):
        app = QApplication(sys.argv)
        self.pp = teacherWindow()
        self.pp.show()
        t=newThread.thread()
        t.start()
        t.showSignal.connect(self.showInfo)
        sys.exit(app.exec_())



