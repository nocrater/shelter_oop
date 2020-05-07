from PyQt5.QtWidgets import QMessageBox

from controllers.animals_controller import AnimalsController
from enums.animal_type import AnimalType
from views.client import *
from pony.orm import *
from models.client import Client
from models.animal import Animal


class ClientController(QtWidgets.QDialog):
    def __init__(self, parent, identifier=None):
        super(ClientController, self).__init__(parent)
        self.ui = Ui_client()
        self.ui.setupUi(self)
        self.setWindowTitle("Client")

        self.num_of_row_giving = 0
        self.num_of_row_taking = 0

        if identifier is not None:
            self.identifier = identifier
            self.is_new = False
            self.init()
        else:
            self.is_new = True

        self.ui.tableWidget_to_give.setHorizontalHeaderLabels(["Id", "Name"])
        self.ui.tableWidget_to_give.setColumnHidden(0, True)

        self.ui.tableWidget_to_take.setHorizontalHeaderLabels(["Id", "Name"])
        self.ui.tableWidget_to_take.setColumnHidden(0, True)

        self.ui.add_to_give.clicked.connect(self.add_to_give)
        self.ui.add_to_take.clicked.connect(self.add_to_take)

        self.ui.delete_to_give.clicked.connect(self.delete_to_give)
        self.ui.delete_to_take.clicked.connect(self.delete_to_take)

        self.ui.ok_button.clicked.connect(self.ok)

    @db_session
    def init(self):
        client = Client[self.identifier]
        self.ui.name_edit.setText(client.name)

        giving_animals = [Animal.get(id=a.id) for a in client.animals_to_give]
        taking_animals = [Animal.get(id=a.id) for a in client.animals_to_take]
        
        for animal in giving_animals:
            self.update_sets(animal.id, animal.name, AnimalType.Giving)

        for animal in taking_animals:
            self.update_sets(animal.id, animal.name, AnimalType.Taking)

    def add_to_give(self):
        animals = AnimalsController(self, selecting=True, animal_type=AnimalType.Giving)
        animals.show()

    def add_to_take(self):
        animals = AnimalsController(self, selecting=True, animal_type=AnimalType.Taking)
        animals.show()

    def delete_to_give(self):
        selection = self.ui.tableWidget_to_give.selectionModel().selectedRows()

        for elem in selection:
            self.ui.tableWidget_to_give.removeRow(elem.row())
            self.num_of_row_giving -= 1

    def delete_to_take(self):
        selection = self.ui.tableWidget_to_take.selectionModel().selectedRows()

        for elem in selection:
            self.ui.tableWidget_to_take.removeRow(elem.row())
            self.num_of_row_taking -= 1

    @db_session
    def ok(self):
        name = self.ui.name_edit.text().strip()

        if name == "":
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Name should not be empty or contains only spaces")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
            return

        indices = []
        for elem in range(self.num_of_row_giving):
            indices.append(int(self.ui.tableWidget_to_give.item(elem, 0).text()))

        giving_animals = [Animal.get(id=i) for i in indices]

        indices = []
        for elem in range(self.num_of_row_taking):
            indices.append(int(self.ui.tableWidget_to_take.item(elem, 0).text()))

        taking_animals = [Animal.get(id=i) for i in indices]

        if self.is_new:
            Client(name=name, animals_to_give=giving_animals, animals_to_take=taking_animals)
        else:
            client = Client[self.identifier]
            client.name = name
            client.animals_to_give = giving_animals
            client.animals_to_take = taking_animals

        self.close()

    @db_session
    def update_sets(self, animal_id, animal_name, animal_type):
        indices = []

        for elem in range(self.num_of_row_giving):
            indices.append(int(self.ui.tableWidget_to_give.item(elem, 0).text()))

        for elem in range(self.num_of_row_taking):
            indices.append(int(self.ui.tableWidget_to_take.item(elem, 0).text()))

        if animal_id in indices:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Client already has this animal in giving or taking group")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
            return

        if animal_type == AnimalType.Giving:
            self.ui.tableWidget_to_give.insertRow(self.num_of_row_giving)

            self.ui.tableWidget_to_give.setItem(self.num_of_row_giving, 0, QtWidgets.QTableWidgetItem(str(animal_id)))
            self.ui.tableWidget_to_give.setItem(self.num_of_row_giving, 1, QtWidgets.QTableWidgetItem(animal_name))

            self.num_of_row_giving += 1

        else:
            self.ui.tableWidget_to_take.insertRow(self.num_of_row_taking)

            self.ui.tableWidget_to_take.setItem(self.num_of_row_taking, 0, QtWidgets.QTableWidgetItem(str(animal_id)))
            self.ui.tableWidget_to_take.setItem(self.num_of_row_taking, 1, QtWidgets.QTableWidgetItem(animal_name))

            self.num_of_row_taking += 1
