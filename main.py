from client import *
from clientTeacher import *
from doorClient import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # client=client()
    # client.do()
    a=teacherWindow()
    a.show()
    sys.exit(app.exec_())