from client import *
from windowStudent import *
from windowDoor import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    client=teacherClient()
    client.do()
    sys.exit(app.exec_())