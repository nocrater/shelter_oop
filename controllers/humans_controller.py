from PyQt5.QtWidgets import QMessageBox

from views.humans import *
from pony.orm import *
from models.human import Human
from controllers.human_controller import HumanController


class HumansController(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(HumansController, self).__init__(parent)
        self.ui = Ui_humans()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self)
        self.setWindowTitle("Humans")

        self.ui.tableWidget.setHorizontalHeaderLabels(["Id", "Name"])

        self.get_humans()

        self.ui.new_button.clicked.connect(self.new_human)
        self.ui.edit_button.clicked.connect(self.edit_human)
        self.ui.delete_button.clicked.connect(self.delete_human)

    @db_session
    def get_humans(self):
        self.ui.tableWidget.setRowCount(0)

        humans = select(h for h in Human)
        for number, human in enumerate(humans):
            self.ui.tableWidget.insertRow(number)

            self.ui.tableWidget.setItem(number, 0, QtWidgets.QTableWidgetItem(str(human.id)))
            self.ui.tableWidget.setItem(number, 1, QtWidgets.QTableWidgetItem(human.name))

    @db_session
    def new_human(self):
        human = HumanController(self)
        human.exec_()

        self.get_humans()

    def edit_human(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        if len(selection) != 1:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Please select 1 row for editing")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
        else:
            elem = selection[0]
            human = HumanController(self, int(self.ui.tableWidget.item(elem.row(), 0).text()))
            human.exec_()

            self.get_humans()

    def delete_human(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        indices = []
        for elem in selection:
            indices.append(int(self.ui.tableWidget.item(elem.row(), 0).text()))

        with db_session:
            delete(h for h in Human if h.id in indices)

        self.get_humans()
