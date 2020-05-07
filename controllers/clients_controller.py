from PyQt5.QtWidgets import QMessageBox

from views.clients import *
from pony.orm import *
from models.client import Client
from controllers.client_controller import ClientController


class ClientsController(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(ClientsController, self).__init__(parent)
        self.ui = Ui_clients()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self)
        self.setWindowTitle("Clients")

        self.ui.tableWidget.setHorizontalHeaderLabels(["Id", "Name"])
        self.ui.tableWidget.setColumnHidden(0, True)

        self.get_clients()

        self.ui.new_button.clicked.connect(self.new_client)
        self.ui.edit_button.clicked.connect(self.edit_client)
        self.ui.delete_button.clicked.connect(self.delete_client)

    @db_session
    def get_clients(self):
        self.ui.tableWidget.setRowCount(0)

        clients = select(h for h in Client)

        for number, client in enumerate(clients):
            self.ui.tableWidget.insertRow(number)

            self.ui.tableWidget.setItem(number, 0, QtWidgets.QTableWidgetItem(str(client.id)))
            self.ui.tableWidget.setItem(number, 1, QtWidgets.QTableWidgetItem(client.name))

    @db_session
    def new_client(self):
        client = ClientController(self)
        client.exec_()

        self.get_clients()

    def edit_client(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        if len(selection) != 1:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Please select 1 row for editing")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
        else:
            elem = selection[0]
            client = ClientController(self, int(self.ui.tableWidget.item(elem.row(), 0).text()))
            client.exec_()

            self.get_clients()

    def delete_client(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        indices = []
        for elem in selection:
            indices.append(int(self.ui.tableWidget.item(elem.row(), 0).text()))

        with db_session:
            delete(h for h in Client if h.id in indices)

        self.get_clients()
