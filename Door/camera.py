import cv2

import numpy as np

import time

import sys

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5 import QtGui
import threading
class cameraThread(QThread):
    def __init__(self,label):
        super().__init__()
        self.lable=label
    def run(self):
        cap=cv2.VideoCapture(0)
        while True:
            sucess,img=cap.read()
            show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.lable.setPixmap(QtGui.QPixmap.fromImage(showImage))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    box = QWidget()
    cameraLayout=QHBoxLayout()
    lable=QLabel()
    cameraLayout.addWidget(lable)
    box.setLayout(cameraLayout)
    box.show()
    t=cameraThread(lable)
    t.start()
    sys.exit(app.exec_())



