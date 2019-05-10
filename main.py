from client import *
from studentClient import *
from doorClient import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    client=client()
    client.do()
    sys.exit(app.exec_())