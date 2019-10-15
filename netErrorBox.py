from PyQt5 import QtCore , QtGui
from PyQt5.QtWidgets import QLabel , QDialog

messageBox=0

def netErrorMessageBoxShow():
    global messageBox
    messageBox = QDialog()
    lable=QLabel(messageBox)
    movie = QtGui.QMovie("./static/teacherimg/robot.gif")
    lable.setMovie(movie)
    movie.start()
    messageBox.setFixedHeight(200)
    messageBox.setFixedWidth(200)
    messageBox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
    messageBox.exec_()

def netErrorMessageBoxClose():
    global messageBox
    messageBox.close()