import PyQt5.QtCore
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import *

from settings import *


class teacherWindow(QWidget):
    ControlSignal = PyQt5.QtCore.pyqtSignal(list)
    ButtonList = []
    FuncList = []
    VisitorList = []

    def __init__(self):
        QWidget.__init__(self)
        WholePalette = QPalette()
        WholePalette.setColor(QPalette.Window, QColor(1, 28, 52))
        self.setPalette(WholePalette)
        # 背景颜色
        WholeLayout = QHBoxLayout()
        # 整体布局

        StudentDataLayout = QVBoxLayout()
        # 学生信息区域布局
        StudentPhoto = self.StudentImgGroundSet()
        StudentDataLayout.addWidget(StudentPhoto)
        # 头像区域
        StudentDetail = self.StudentDataGroundSet()
        StudentDataLayout.addWidget(StudentDetail)
        # 详细信息区域

        SeparateWiget = self.SeparateGroundSet()
        # 中间分隔区域

        StudentRecordLayout = self.TableGroundSet()
        # 表格区域布局
        StudentRecordGround = QWidget()
        StudentRecordGround.setStyleSheet(
            TEACHERCLIENT_RECORDGROUND_STYLE)
        StudentRecordGround.setLayout(StudentRecordLayout)
        # 表格区域

        WholeLayout.addLayout(StudentDataLayout)
        WholeLayout.addWidget(SeparateWiget)
        WholeLayout.addWidget(StudentRecordGround)
        self.setLayout(WholeLayout)

    def StudentImgGroundSet(self):
        PhotoBackground = QWidget()  # 头像底图区域
        PhotoBackground.setFixedHeight(
            TEACHERCLIENT_SCREEN_HEIGHT *
            PHOTOBACKGROUND_HEIGHT_PROPORTION)
        PhotoBackground.setFixedWidth(
            TEACHERCLIENT_SCREEN_WIDTH *
            PHOTOBACKGROUND_WIDTH_PROPORTION)
        PhotoBackground.setStyleSheet(
            TEACHERCLIENT_PHOTOGROUND_STYLE)

        PhotoBackgroundLayout = QVBoxLayout()  # 底图布局
        PhotoBackgroundLayout.setAlignment(PyQt5.QtCore.Qt.AlignHCenter)

        self.Photo = QWidget()  # 头像
        self.Photo.setFixedHeight(
            TEACHERCLIENT_SCREEN_HEIGHT *
            PHOTO_HEIGHT_PROPORTION)
        self.Photo.setFixedWidth(
            TEACHERCLIENT_SCREEN_HEIGHT *
            PHOTO_WIDTH_PROPORTION)
        self.Photo.setStyleSheet(
            TEACHERCLIENT_PHOTO_STYLE)

        PhotoBackgroundLayout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        PhotoBackgroundLayout.addWidget(self.Photo)
        PhotoBackground.setLayout(PhotoBackgroundLayout)
        return PhotoBackground

    def StudentDataGroundSet(self):
        """
        学生详细信息区域
        :return:
        """
        def WordSet(lable):
            lable.setFont(QFont("微软雅黑", 13, QFont.Bold))
            lable.setStyleSheet('color:rgb(207, 214, 218)')

        self.DataGround = QWidget()
        self.DataGround.setFixedWidth(
            TEACHERCLIENT_SCREEN_WIDTH *
            DATAGROUND_WIDTH_PROPORTION)
        self.DataGround.setFixedHeight(
            TEACHERCLIENT_SCREEN_HEIGHT *
            DATAGROUND_HEIGHT_PROPORTION)
        self.DataGround.setAutoFillBackground(True)

        DataGroundPalette = QPalette()
        DataGroundPalette.setBrush(
            QPalette.Background, QBrush(
                QPixmap("./static/teacherimg/信息底图.png")))
        self.DataGround.setPalette(DataGroundPalette)

        DataGroundLayout = QGridLayout()

        empty = QLabel("")
        WordSet(empty)
        empty.setFixedWidth(150)
        DataGroundLayout.addWidget(empty, 0, 0, 1, 1)

        self.nameLable = QLabel("")
        WordSet(self.nameLable)
        DataGroundLayout.addWidget(self.nameLable, 1, 1, 1, 3)

        empty = QLabel("")
        empty.setFixedWidth(220)
        DataGroundLayout.addWidget(empty, 1, 4, 1, 1)

        self.classLable = QLabel("")
        WordSet(self.classLable)
        DataGroundLayout.addWidget(self.classLable, 1, 5, 1, 2)

        self.idnumber = QLabel("")
        WordSet(self.idnumber)
        DataGroundLayout.addWidget(self.idnumber, 2, 1, 1, 3)

        self.score = QLabel("")
        WordSet(self.score)
        DataGroundLayout.addWidget(self.score, 2, 5, 1, 2)

        self.phonenumber = QLabel("")
        WordSet(self.phonenumber)
        DataGroundLayout.addWidget(self.phonenumber, 3, 1, 1, 3)

        empty = QLabel("")
        DataGroundLayout.addWidget(empty, 3, 5, 1, 1)

        self.parentphonenumber = QLabel("")
        self.parentphonenumber.setMaximumHeight(80)
        WordSet(self.parentphonenumber)
        DataGroundLayout.addWidget(self.parentphonenumber, 3, 6, 1, 3)

        empty = QLabel("")
        empty.setFixedWidth(80)
        DataGroundLayout.addWidget(empty , 4 , 1 , 1 , 1)

        self.province = QLabel("")
        WordSet(self.province)
        DataGroundLayout.addWidget(self.province, 4, 2, 1, 2)

        self.party = QLabel("")
        self.party.setMaximumHeight(80)
        WordSet(self.party)
        DataGroundLayout.addWidget(self.party, 4, 6, 1, 3)

        self.address = QLabel("")
        WordSet(self.address)
        DataGroundLayout.addWidget(self.address, 5, 2, 1, 7)

        self.other = QLabel("")
        WordSet(self.other)
        DataGroundLayout.addWidget(self.other, 6, 2, 1, 7)

        self.DataGround.setLayout(DataGroundLayout)

        return self.DataGround

    def SeparateGroundSet(self):
        """
        中间分隔区域
        :return:
        """
        SeparateWiget = QWidget()
        SeparateWiget.setFixedWidth(
            TEACHERCLIENT_SCREEN_WIDTH *
            SEPERATEGROUND_WIDTH_PROPORTION)
        SeparateWiget.setStyleSheet(
            TEACHERCLIENT_SEPERATE_STYLE)
        return SeparateWiget

    def TableGroundSet(self):
        """
        访客列表区域
       :return:
        """
        TableGroundLayout = QVBoxLayout()

        self.TableGround = QTableWidget(RECORD_ROWNUM, RECORD_COLUMNUM)
        self.TableGround.setStyleSheet(
            TEACHERCLIENT_TABLE_STYLE)
        self.TableGround.verticalHeader().setVisible(False)  # 纵向表头隐藏
        self.TableGround.horizontalHeader().setVisible(False)  # 横向表头隐藏

        self.TableGround.setSelectionMode(
            QAbstractItemView.NoSelection)  # 不可选中，以免点击之后反色

        self.TableGround.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)  # 自动伸缩适应大小
        self.TableGround.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 同上

        self.TableGround.setEditTriggers(
            QAbstractItemView.NoEditTriggers)  # 不可编辑

        self.ButtonSet()

        TableGroundLayout.addWidget(self.TableGround)
        TableGroundLayout.addLayout(self.BannerGroundSet())

        return TableGroundLayout

    def ButtonSet(self):
        """
        表格内按钮设置
        :return:
        """
        for index in range(RECORD_ROWNUM):  # 初始化Button
            TableButtonLayout = QVBoxLayout()
            TableButtonLayout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

            TableButtonWiget = QWidget()

            Button = QPushButton("显示")
            Button.setFixedWidth(
                TEACHERCLIENT_SCREEN_WIDTH *
                TABLE_BUTTON_WIDTH_PROPORTION)
            Button.setFixedHeight(
                TEACHERCLIENT_SCREEN_HEIGHT *
                TABLE_BUTTON_HEIGHT_PROPORTION)
            Button.setStyleSheet(TEACHERCLIENT_BUTTON_STYLE)

            TableButtonLayout.addWidget(Button)
            TableButtonWiget.setLayout(TableButtonLayout)
            self.TableGround.setCellWidget(index, 3, TableButtonWiget)

            self.FuncList.append(self.makeFunc(index))
            self.ButtonList.append(Button)
            self.ButtonList[index].clicked.connect(self.FuncList[index])

    def BannerGroundSet(self):
        """
        下方按钮与选栏区域布局
        :return:
        """
        BannerLayout = QHBoxLayout()

        PageNumberTip = QLabel("页码")
        PageNumberTip.setStyleSheet(TEACHERCLIENT_LABLE_STYLE)

        self.PageNum = QLabel("1")
        self.PageNum.setFixedWidth(
            TEACHERCLIENT_SCREEN_WIDTH *
            TABLE_PAGELABLE_WIDTH_PROPORTION)
        self.PageNum.setStyleSheet(TEACHERCLIENT_LABLE_STYLE)

        BannerLayout.addWidget(PageNumberTip)
        BannerLayout.addWidget(self.PageNum)
        BannerLayout.addWidget(self.ComboboxSet())
        BannerLayout.addWidget(self.ComboboxButtonSet())
        BannerLayout.addWidget(self.PreButtonSet())
        BannerLayout.addWidget(self.BackButtonSet())

        self.ControlSignal.connect(self.page_controller)
        return BannerLayout

    def ComboboxSet(self):
        """
        下拉选栏
        :return:
        """
        self.Combobox = QComboBox()
        self.Combobox.setFixedHeight(
            TEACHERCLIENT_SCREEN_WIDTH *
            TABLE_PRE_OR_BACK_BUTTON_HEIGHT_PROPORTION -
            10)
        self.Combobox.setFixedWidth(TEACHERCLIENT_SCREEN_WIDTH *
                                    TABLE_PRE_OR_BACK_BUTTON_WIDTH_PROPORTION)
        self.Combobox.setStyleSheet(TEACHERCLIENT_COMBOBOX_STYLE)
        self.Combobox.addItems(["全部", "2015", "2016", "2017", "2018"])
        return self.Combobox

    def ComboboxButtonSet(self):
        """
        选栏按钮
        :return:
        """
        button = QPushButton("确认")
        button.setFixedHeight(TEACHERCLIENT_SCREEN_WIDTH *
                              TABLE_PRE_OR_BACK_BUTTON_HEIGHT_PROPORTION)
        button.setFixedWidth(TEACHERCLIENT_SCREEN_WIDTH *
                             TABLE_PRE_OR_BACK_BUTTON_WIDTH_PROPORTION)
        button.setStyleSheet(TEACHERCLIENT_BUTTON_STYLE)
        button.clicked.connect(self.UpdateGrade)
        return button

    def PreButtonSet(self):
        """
        上一页按钮
        :return:
        """
        self.PrevButton = QPushButton("前一页")
        self.PrevButton.setFixedHeight(
            TEACHERCLIENT_SCREEN_WIDTH *
            TABLE_PRE_OR_BACK_BUTTON_HEIGHT_PROPORTION)
        self.PrevButton.setFixedWidth(
            TEACHERCLIENT_SCREEN_WIDTH *
            TABLE_PRE_OR_BACK_BUTTON_WIDTH_PROPORTION)
        self.PrevButton.setStyleSheet(TEACHERCLIENT_BUTTON_STYLE)
        self.PrevButton.clicked.connect(self.PrePage)

        return self.PrevButton

    def BackButtonSet(self):
        """
        下一页按钮
        :return:
        """
        self.BackButton = QPushButton("后一页")
        self.BackButton.setFixedHeight(
            TEACHERCLIENT_SCREEN_WIDTH *
            TABLE_PRE_OR_BACK_BUTTON_HEIGHT_PROPORTION)
        self.BackButton.setFixedWidth(
            TEACHERCLIENT_SCREEN_WIDTH *
            TABLE_PRE_OR_BACK_BUTTON_WIDTH_PROPORTION)
        self.BackButton.clicked.connect(self.BackPage)
        self.BackButton.setStyleSheet(TEACHERCLIENT_BUTTON_STYLE)
        return self.BackButton
