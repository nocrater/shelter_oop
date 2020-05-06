from views.client import *
from pony.orm import *
from models.client import Client


class ClientController(QtWidgets.QDialog):
    def __init__(self, parent, identifier=None):
        super(ClientController, self).__init__(parent)
        self.ui = Ui_client()
        self.ui.setupUi(self)
        self.setWindowTitle("Client")

        if identifier is not None:
            self.identifier = identifier
            self.is_new = False
            self.init()
        else:
            self.is_new = True

        self.ui.ok_button.clicked.connect(self.ok)

    @db_session
    def init(self):
        client = Client[self.identifier]
        self.ui.name_edit.setText(client.name)

    @db_session
    def ok(self):
        if self.is_new:
            Client(name=self.ui.name_edit.text())
        else:
            client = Client[self.identifier]
            client.name = self.ui.name_edit.text()

        self.close()
