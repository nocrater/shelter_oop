# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nocrater\PycharmProjects\Shelter\uis\humans.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_humans(object):
    def setupUi(self, humans):
        humans.setObjectName("humans")
        humans.resize(800, 709)
        self.centralwidget = QtWidgets.QWidget(humans)
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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(260)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(70)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        humans.setCentralWidget(self.centralwidget)

        self.retranslateUi(humans)
        QtCore.QMetaObject.connectSlotsByName(humans)

    def retranslateUi(self, humans):
        _translate = QtCore.QCoreApplication.translate
        humans.setWindowTitle(_translate("humans", "MainWindow"))
        self.new_button.setText(_translate("humans", "New"))
        self.edit_button.setText(_translate("humans", "Edit"))
        self.delete_button.setText(_translate("humans", "Delete"))
