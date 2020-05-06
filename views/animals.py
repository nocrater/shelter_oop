# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nocrater\PycharmProjects\Shelter\uis\animals.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_animals(object):
    def setupUi(self, animals):
        animals.setObjectName("animals")
        animals.resize(1325, 764)
        self.centralwidget = QtWidgets.QWidget(animals)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 25, -1, 25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_button.sizePolicy().hasHeightForWidth())
        self.new_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_button.setFont(font)
        self.new_button.setObjectName("new_button")
        self.horizontalLayout_2.addWidget(self.new_button)
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_button.setFont(font)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout_2.addWidget(self.edit_button)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(260)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        animals.setCentralWidget(self.centralwidget)

        self.retranslateUi(animals)
        QtCore.QMetaObject.connectSlotsByName(animals)

    def retranslateUi(self, animals):
        _translate = QtCore.QCoreApplication.translate
        animals.setWindowTitle(_translate("animals", "MainWindow"))
        self.new_button.setText(_translate("animals", "New"))
        self.edit_button.setText(_translate("animals", "Edit"))
        self.delete_button.setText(_translate("animals", "Delete"))
