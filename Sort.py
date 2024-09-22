# Form implementation generated from reading ui file 'Sort.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sorting(object):
    def setupUi(self, Sorting):
        Sorting.setObjectName("Sorting")
        Sorting.resize(1550, 1000)
        Sorting.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=Sorting)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 101, 951))
        self.widget.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.widget.setStyleSheet("background-color: rgb(0, 67, 9);\n"
"boorder-radius:10px;")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget)
        self.widget_4.setMaximumSize(QtCore.QSize(200, 1000))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_3.setMaximumSize(QtCore.QSize(60, 60))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/cropped_image.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.widget_4)
        self.pushButton_home = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setStyleSheet("\n"
"background-color: transparent;\n"
"color:black;\n"
"\n"
"")
        self.pushButton_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/home-2.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.pushButton_home.setIcon(icon)
        self.pushButton_home.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout.addWidget(self.pushButton_home)
        self.pushButton_search = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("\n"
"background-color: transparent;\n"
"color:black;\n"
"\n"
"")
        self.pushButton_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/search-interface-symbol.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.pushButton_search.setIcon(icon1)
        self.pushButton_search.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout.addWidget(self.pushButton_search)
        self.pushButton_setting = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_setting.setFont(font)
        self.pushButton_setting.setStyleSheet("\n"
"background-color: transparent;\n"
"color:black;\n"
"\n"
"")
        self.pushButton_setting.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/settings.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.pushButton_setting.setIcon(icon2)
        self.pushButton_setting.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.verticalLayout.addWidget(self.pushButton_setting)
        self.pushButton_game = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_game.setFont(font)
        self.pushButton_game.setStyleSheet("\n"
"background-color: transparent;\n"
"color:black;\n"
"\n"
"")
        self.pushButton_game.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Downloads/bar-chart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_game.setIcon(icon3)
        self.pushButton_game.setIconSize(QtCore.QSize(29, 29))
        self.pushButton_game.setObjectName("pushButton_game")
        self.verticalLayout.addWidget(self.pushButton_game)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_8 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(240, 0, 311, 121))
        self.widget_8.setStyleSheet("background-color: transparent;\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_sortLatest = QtWidgets.QPushButton(parent=self.widget_8)
        self.pushButton_sortLatest.setStyleSheet("background-color: rgb(0, 183, 0);")
        self.pushButton_sortLatest.setObjectName("pushButton_sortLatest")
        self.horizontalLayout_3.addWidget(self.pushButton_sortLatest)
        self.pushButton_sortAZ = QtWidgets.QPushButton(parent=self.widget_8)
        self.pushButton_sortAZ.setStyleSheet("background-color: rgb(0, 183, 0);")
        self.pushButton_sortAZ.setObjectName("pushButton_sortAZ")
        self.horizontalLayout_3.addWidget(self.pushButton_sortAZ)
        self.pushButton_sortTop = QtWidgets.QPushButton(parent=self.widget_8)
        self.pushButton_sortTop.setStyleSheet("background-color: rgb(0, 183, 0);")
        self.pushButton_sortTop.setObjectName("pushButton_sortTop")
        self.horizontalLayout_3.addWidget(self.pushButton_sortTop)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(210, 90, 1101, 481))
        self.scrollArea.setMinimumSize(QtCore.QSize(741, 461))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1099, 464))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.widget_2.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_2.setStyleSheet("background-color: transparent;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_12 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_12.setMinimumSize(QtCore.QSize(214, 377))
        self.widget_12.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_12.setStyleSheet("background-color: transparent;")
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_12)
        self.label_14.setMaximumSize(QtCore.QSize(1111111, 111111))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("../../Downloads/Rolling in the deep.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(parent=self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:white;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_6.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(parent=self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:grey;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_28 = QtWidgets.QLabel(parent=self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:rgb(0, 126, 0);")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_6.addWidget(self.label_28)
        self.pushButton_play = QtWidgets.QPushButton(parent=self.widget_12)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Downloads/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_play.setIcon(icon4)
        self.pushButton_play.setIconSize(QtCore.QSize(61, 42))
        self.pushButton_play.setObjectName("pushButton_play")
        self.verticalLayout_6.addWidget(self.pushButton_play)
        self.horizontalLayout.addWidget(self.widget_12)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout.addWidget(self.widget_6)
        self.widget_13 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_13.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_13.setStyleSheet("background-color: transparent;")
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_20 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_20.setMaximumSize(QtCore.QSize(1111111, 111111))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("../../Downloads/Bliding lights.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(parent=self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:white;")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_8.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(parent=self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:grey;")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.label_27 = QtWidgets.QLabel(parent=self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:rgb(0, 126, 0);")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_8.addWidget(self.label_27)
        self.pushButton_play1 = QtWidgets.QPushButton(parent=self.widget_13)
        self.pushButton_play1.setIcon(icon4)
        self.pushButton_play1.setIconSize(QtCore.QSize(61, 42))
        self.pushButton_play1.setObjectName("pushButton_play1")
        self.verticalLayout_8.addWidget(self.pushButton_play1)
        self.horizontalLayout.addWidget(self.widget_13)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout.addWidget(self.widget_7)
        self.widget_14 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_14.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_14.setStyleSheet("background-color: transparent;")
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_23 = QtWidgets.QLabel(parent=self.widget_14)
        self.label_23.setMaximumSize(QtCore.QSize(1111111, 111111))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("../../Downloads/shape of you.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_9.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:white;")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_9.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:grey;")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_9.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(parent=self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:rgb(0, 126, 0);")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_9.addWidget(self.label_26)
        self.pushButton_play2 = QtWidgets.QPushButton(parent=self.widget_14)
        self.pushButton_play2.setIcon(icon4)
        self.pushButton_play2.setIconSize(QtCore.QSize(61, 42))
        self.pushButton_play2.setObjectName("pushButton_play2")
        self.verticalLayout_9.addWidget(self.pushButton_play2)
        self.horizontalLayout.addWidget(self.widget_14)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.widget_16 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_16.setGeometry(QtCore.QRect(380, 620, 214, 377))
        self.widget_16.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_16.setStyleSheet("background-color: transparent;")
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_38 = QtWidgets.QLabel(parent=self.widget_16)
        self.label_38.setMaximumSize(QtCore.QSize(1111111, 111111))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("Images/Girls like you.png"))
        self.label_38.setScaledContents(True)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_12.addWidget(self.label_38)
        self.label_39 = QtWidgets.QLabel(parent=self.widget_16)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color:white;")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_12.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(parent=self.widget_16)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color:grey;")
        self.label_40.setObjectName("label_40")
        self.verticalLayout_12.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(parent=self.widget_16)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color:rgb(0, 126, 0);")
        self.label_41.setObjectName("label_41")
        self.verticalLayout_12.addWidget(self.label_41)
        self.widget_15 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_15.setGeometry(QtCore.QRect(120, 620, 214, 377))
        self.widget_15.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_15.setStyleSheet("background-color: transparent;")
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_42 = QtWidgets.QLabel(parent=self.widget_15)
        self.label_42.setMaximumSize(QtCore.QSize(1111111, 111111))
        self.label_42.setText("")
        self.label_42.setPixmap(QtGui.QPixmap("Images/Despacito.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_13.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(parent=self.widget_15)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color:white;")
        self.label_43.setObjectName("label_43")
        self.verticalLayout_13.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(parent=self.widget_15)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color:grey;")
        self.label_44.setObjectName("label_44")
        self.verticalLayout_13.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(parent=self.widget_15)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color:rgb(0, 126, 0);")
        self.label_45.setObjectName("label_45")
        self.verticalLayout_13.addWidget(self.label_45)
        self.widget_17 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_17.setGeometry(QtCore.QRect(610, 620, 214, 377))
        self.widget_17.setMaximumSize(QtCore.QSize(9999, 9999))
        self.widget_17.setStyleSheet("background-color: transparent;")
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_17)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_46 = QtWidgets.QLabel(parent=self.widget_17)
        self.label_46.setMaximumSize(QtCore.QSize(1111111, 111111))
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap("Images/Levitating.png"))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_14.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(parent=self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color:white;")
        self.label_47.setObjectName("label_47")
        self.verticalLayout_14.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(parent=self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color:grey;")
        self.label_48.setObjectName("label_48")
        self.verticalLayout_14.addWidget(self.label_48)
        self.label_49 = QtWidgets.QLabel(parent=self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color:rgb(0, 126, 0);")
        self.label_49.setObjectName("label_49")
        self.verticalLayout_14.addWidget(self.label_49)
        Sorting.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Sorting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1550, 24))
        self.menubar.setObjectName("menubar")
        Sorting.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Sorting)
        self.statusbar.setObjectName("statusbar")
        Sorting.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=Sorting)
        self.toolBar.setObjectName("toolBar")
        Sorting.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(Sorting)
        QtCore.QMetaObject.connectSlotsByName(Sorting)

    def retranslateUi(self, Sorting):
        _translate = QtCore.QCoreApplication.translate
        Sorting.setWindowTitle(_translate("Sorting", "MainWindow"))
        self.pushButton_sortLatest.setText(_translate("Sorting", "Latest"))
        self.pushButton_sortAZ.setText(_translate("Sorting", "A-Z"))
        self.pushButton_sortTop.setText(_translate("Sorting", "Top Music"))
        self.label_15.setText(_translate("Sorting", "Rolling in the deep"))
        self.label_16.setText(_translate("Sorting", "Adelle"))
        self.label_28.setText(_translate("Sorting", "Rating 9.5/10"))
        self.pushButton_play.setText(_translate("Sorting", "               PushButton"))
        self.label_21.setText(_translate("Sorting", "Blinding lights"))
        self.label_22.setText(_translate("Sorting", "The Weeknd"))
        self.label_27.setText(_translate("Sorting", "Rating 10/10"))
        self.pushButton_play1.setText(_translate("Sorting", "               PushButton"))
        self.label_24.setText(_translate("Sorting", "Shape of you"))
        self.label_25.setText(_translate("Sorting", "Ed Sheeran"))
        self.label_26.setText(_translate("Sorting", "Rating 9/10"))
        self.pushButton_play2.setText(_translate("Sorting", "               PushButton"))
        self.label_39.setText(_translate("Sorting", "Girls like you"))
        self.label_40.setText(_translate("Sorting", "Maroon 5"))
        self.label_41.setText(_translate("Sorting", "Rating 8.9/10"))
        self.label_43.setText(_translate("Sorting", "Despacito"))
        self.label_44.setText(_translate("Sorting", "Luis Fonsi"))
        self.label_45.setText(_translate("Sorting", "Rating 9.5/10"))
        self.label_47.setText(_translate("Sorting", "Levitating"))
        self.label_48.setText(_translate("Sorting", "Dua Lipa"))
        self.label_49.setText(_translate("Sorting", "Rating 9.2/10"))
        self.toolBar.setWindowTitle(_translate("Sorting", "toolBar"))
