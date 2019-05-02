from client import *
from clientStudent import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # client=client()
    # client.do()
    a=studentWindow()
    a.show()
    sys.exit(app.exec_())