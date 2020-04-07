# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nocrater\PycharmProjects\Shelter\uis\human.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_human(object):
    def setupUi(self, human):
        human.setObjectName("human")
        human.resize(385, 223)
        self.verticalLayout = QtWidgets.QVBoxLayout(human)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(human)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.name_edit = QtWidgets.QLineEdit(human)
        self.name_edit.setObjectName("name_edit")
        self.horizontalLayout_2.addWidget(self.name_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_button = QtWidgets.QPushButton(human)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(100, 0))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(human)
        QtCore.QMetaObject.connectSlotsByName(human)

    def retranslateUi(self, human):
        _translate = QtCore.QCoreApplication.translate
        human.setWindowTitle(_translate("human", "Dialog"))
        self.label.setText(_translate("human", "Name:   "))
        self.ok_button.setText(_translate("human", "OK"))
