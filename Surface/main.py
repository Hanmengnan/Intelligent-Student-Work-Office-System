from Surface.client import *
from Surface.windowStudent import *
from Door.windowDoor import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    client=teacherClient()
    client.do()
    sys.exit(app.exec_())