import sys

from clientDoor import *

from clientStudent import *
from clientTeacher import *
from clientDoor import *
from clock import *
if __name__ == "__main__":
    app=QApplication(sys.argv)
    newWindow= studentWindow()
    newWindow.show()
    p=doorWindow()
    p.show()
    pp=teacherWindow()
    pp.show()
    sys.exit(app.exec_())