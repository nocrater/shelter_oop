# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nocrater\PycharmProjects\Shelter\uis\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 378)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 25, -1, 25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setWordWrap(False)
        self.main_label.setObjectName("main_label")
        self.horizontalLayout.addWidget(self.main_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 25, -1, 25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.humans_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.humans_button.sizePolicy().hasHeightForWidth())
        self.humans_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humans_button.setFont(font)
        self.humans_button.setObjectName("humans_button")
        self.horizontalLayout_2.addWidget(self.humans_button)
        self.clients_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clients_button.sizePolicy().hasHeightForWidth())
        self.clients_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clients_button.setFont(font)
        self.clients_button.setObjectName("clients_button")
        self.horizontalLayout_2.addWidget(self.clients_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 25, -1, 25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.animals_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.animals_button.sizePolicy().hasHeightForWidth())
        self.animals_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.animals_button.setFont(font)
        self.animals_button.setObjectName("animals_button")
        self.horizontalLayout_3.addWidget(self.animals_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.main_label.setText(_translate("main", "Choose which table to edit:"))
        self.humans_button.setText(_translate("main", "Humans"))
        self.clients_button.setText(_translate("main", "Clients"))
        self.animals_button.setText(_translate("main", "Animals"))
