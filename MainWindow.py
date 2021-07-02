from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 980, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(spacerItem)
        self.horizontalLayout_name = QtWidgets.QHBoxLayout()
        self.horizontalLayout_name.setObjectName("horizontalLayout_name")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_name.addItem(spacerItem1)
        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_name.addWidget(self.label_name)
        self.label_name.setStyleSheet("background-color:#ffffff;")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_name.addItem(spacerItem2)
        self.verticalLayout_main.addLayout(self.horizontalLayout_name)
        self.horizontalLayout_button = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button.setObjectName("horizontalLayout_button")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_button.addItem(spacerItem3)
        self.pushButton_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet('background: rgb(6,22,108); color: rgb(255,255,255)')
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_button.addWidget(self.pushButton_start)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_button.addItem(spacerItem4)
        self.verticalLayout_main.addLayout(self.horizontalLayout_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_main.addItem(spacerItem5)
        MainWindow.setCentralWidget(self.verticalLayoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PBSS"))
        self.label_name.setText(_translate("MainWindow", "Polar bears searching system"))
        self.pushButton_start.setText(_translate("MainWindow", "  Загрузить изображения  "))
