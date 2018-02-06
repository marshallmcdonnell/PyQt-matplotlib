# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plotview(object):
    def setupUi(self, plotview):
        plotview.setObjectName("plotview")
        plotview.resize(934, 540)
        self.centralwidget = QtWidgets.QWidget(plotview)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start = QtWidgets.QPushButton(self.groupBox_2)
        self.start.setObjectName("start")
        self.verticalLayout.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.groupBox_2)
        self.stop.setObjectName("stop")
        self.verticalLayout.addWidget(self.stop)
        self.save = QtWidgets.QPushButton(self.groupBox_2)
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)
        self.clear = QtWidgets.QPushButton(self.groupBox_2)
        self.clear.setObjectName("clear")
        self.verticalLayout.addWidget(self.clear)
        self.exit = QtWidgets.QPushButton(self.groupBox_2)
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 1, 1, 1)
        plotview.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(plotview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 21))
        self.menubar.setObjectName("menubar")
        plotview.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(plotview)
        self.statusbar.setObjectName("statusbar")
        plotview.setStatusBar(self.statusbar)

        self.retranslateUi(plotview)
        self.exit.clicked.connect(plotview.close)
        QtCore.QMetaObject.connectSlotsByName(plotview)

    def retranslateUi(self, plotview):
        _translate = QtCore.QCoreApplication.translate
        plotview.setWindowTitle(_translate("plotview", "MainWindow"))
        self.start.setText(_translate("plotview", "Start"))
        self.stop.setText(_translate("plotview", "Stop"))
        self.save.setText(_translate("plotview", "Save Data"))
        self.clear.setText(_translate("plotview", "Clear Data"))
        self.exit.setText(_translate("plotview", "Exit"))

