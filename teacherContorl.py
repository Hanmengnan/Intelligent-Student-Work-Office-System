from PyQt5.QtCore import Qt

from teacherWindow import *
from database import *

import newThread
class teacherControl(teacherWindow):
    def __init__(self):
        teacherWindow.__init__(self)
        self.showFullScreen()
        self.UpdateGrade()

    def UpdateGrade(self):
        Grade = self.Combobox.currentText()
        file = open("./temp/grade.txt", "w")
        file.write(Grade)
        file.close()
        self.MainPageShow()
        self.PageNum.setText("1")

    def PrePage(self):
        """
        点击上一页信号
        """
        self.ControlSignal.emit(["pre", self.PageNum.text()])

    def BackPage(self):
        """
        点击下一页信号
        """
        self.ControlSignal.emit(["back", self.PageNum.text()])

    def page_controller(self, signal):
        """
        翻页控制
        :param signal:
        :return:
        """

        TotalPage = self.GetPageCount()
        CurrentPageNum = int(signal[1])

        if "pre" == signal[0]:
            if 1 == int(signal[1]):
                return
            self.PageNum.setText(str(CurrentPageNum - 1))
        elif "back" == signal[0]:
            if TotalPage == int(signal[1]):


                return
            self.PageNum.setText(str(CurrentPageNum + 1))

        self.ChangePage(int(self.PageNum.text()))  # 改变表格内容

    def GetPageCount(self):
        return (DataCount() + RECORD_ROWNUM - 1) // RECORD_ROWNUM

    def MainPageShow(self):
        self.ChangePage(1)
        self.ShowFirstVisitor()
    def ChangePage(self, pageindex):
        try:
            self.VisitorList = ChangePage(pageindex)
        except BaseException:
            pass
        for index in range(RECORD_ROWNUM):
            self.TableGround.setItem(index, 0, QTableWidgetItem(""))
            self.TableGround.setItem(index, 1, QTableWidgetItem(""))
            self.TableGround.setItem(index, 2, QTableWidgetItem(""))

        RecordFont = QFont()
        RecordFont.setPointSize(15)

        def RecoordItemSet(item):
            item.setTextAlignment(Qt.AlignCenter)
            item.setFont(RecordFont)
            item.setForeground(QBrush(QColor(255, 255, 255)))
            return item
        for index in range(len(self.VisitorList)):
            Id = QTableWidgetItem(str(self.VisitorList[index][0]))
            RecoordItemSet(Id)
            self.TableGround.setItem(index, 0, Id)

            Name = QTableWidgetItem(str(self.VisitorList[index][1]))
            RecoordItemSet(Name)
            self.TableGround.setItem(index, 1, Name)

            Time = QTableWidgetItem(self.VisitorList[index][2])
            RecoordItemSet(Time)
            self.TableGround.setItem(index, 2, Time)
        self.ShowFirstVisitor()

    def makeFunc(self, index):

        def DetailShow():
            if (self.TableGround.item(index, 0) is not None):  # 学号不为空
                StuId = self.TableGround.item(index, 0).text()
                Data = Detail(StuId)  # 利用学号查询详细信息
                if Data != {}:
                    self.nameLable.setText(Data["xm"])
                    self.classLable.setText(Data["bj"])
                    self.phonenumber.setText(Data["dh"])
                    self.idnumber.setText(Data["xh"])
                    self.parentphonenumber.setText(Data["jzdh"])
                    self.province.setText(Data["jg"])
                    self.address.setText(Data["dz"])
                    self.party.setText(Data["zz"])
                    self.other.setText(Data["bz"])
                    if GetPhoto(StuId):
                        self.Photo.setStyleSheet(
                        TEACHERCLIENT_PHOTOEMPTY_STYLE)
                    else:  # 有信息无照片，照片置空
                        self.PhotoSetEmpty()
                else:
                    # 查不到信息，全部置空
                    self.DetailSetEmpty()
                    self.PhotoSetEmpty()
            else:
                self.DetailSetEmpty()
                self.PhotoSetEmpty()

        return DetailShow


    def DetailSetEmpty(self):
        self.nameLable.setText("")
        self.classLable.setText("")
        self.phonenumber.setText("")
        self.idnumber.setText("")
        self.parentphonenumber.setText("")
        self.province.setText("")
        self.address.setText("")

    def PhotoSetEmpty(self):
        self.Photo.setStyleSheet(
            "QWidget{border-image:url(./teacherimg/头像.png);}")

    def ShowFirstVisitor(self):

        if (self.TableGround.item(0 , 0) is not None):  # 学号不为空

            StuId = self.TableGround.item(0 , 0).text()
            Data = Detail(StuId)  # 利用学号查询详细信息
            if Data != {}:
                self.nameLable.setText(Data["xm"])
                self.classLable.setText(Data["bj"])
                self.phonenumber.setText(Data["dh"])
                self.idnumber.setText(Data["xh"])
                self.parentphonenumber.setText(Data["jzdh"])
                self.province.setText(Data["jg"])
                self.address.setText(Data["dz"])
                # self.party.setText()
                if GetPhoto(StuId):
                    self.Photo.setStyleSheet(
                        TEACHERCLIENT_PHOTOEMPTY_STYLE)
                else:  # 有信息无照片，照片置空
                    self.PhotoSetEmpty()
            else:
                # 查不到信息，全部置空
                self.DetailSetEmpty()
                self.PhotoSetEmpty()
        else:
            self.DetailSetEmpty()
            self.PhotoSetEmpty()

