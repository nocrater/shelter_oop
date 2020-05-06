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