from Door.client import *

from Door.windowDoor import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    client=doorClient()
    client.do()
    sys.exit(app.exec_())
