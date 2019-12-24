from PyQt5 import QtCore , QtGui , Qt
from PyQt5.QtWidgets import QLabel , QDialog

messageBox=0

def netErrorMessageBoxShow():
    global messageBox
    messageBox = QDialog()
    lable=QLabel(messageBox)
    movie = QtGui.QMovie("./static/teacherimg/g.gif")
    lable.setMovie(movie)
    movie.start()
    messageBox.setFixedHeight(200)
    messageBox.setFixedWidth(200)
    messageBox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
    messageBox.exec_()

def netErrorMessageBoxClose():
    try:
        global messageBox
        if not messageBox==0:
            messageBox.close()
    except:
        pass