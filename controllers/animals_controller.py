from PyQt5.QtWidgets import QMessageBox

from views.animals import *
from pony.orm import *
from models.animal import Animal
from controllers.animal_controller import AnimalController


class AnimalsController(QtWidgets.QMainWindow):
    def __init__(self, parent, selecting=None, animal_type=None):
        super(AnimalsController, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_animals()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self)
        self.setWindowTitle("Animals")

        self.ui.tableWidget.setHorizontalHeaderLabels(["Id", "Name", "Description", "Species", "State", "Where now"])
        self.ui.tableWidget.setColumnHidden(0, True)

        self.get_animals()

        self.ui.new_button.clicked.connect(self.new_animal)
        self.ui.edit_button.clicked.connect(self.edit_animal)
        self.ui.delete_button.clicked.connect(self.delete_animal)

        if selecting and animal_type:
            self.animal_type = animal_type

            horizontalLayout = QtWidgets.QHBoxLayout()
            horizontalLayout.setObjectName("horizontalLayout")

            select_button = QtWidgets.QPushButton("Select")

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(select_button.sizePolicy().hasHeightForWidth())

            select_button.setSizePolicy(sizePolicy)
            select_button.setMinimumSize(QtCore.QSize(100, 0))
            select_button.setObjectName("ok_button")

            horizontalLayout.addWidget(select_button)
            self.ui.verticalLayout.addLayout(horizontalLayout)

            select_button.clicked.connect(self.select)

    @db_session
    def get_animals(self):
        self.ui.tableWidget.setRowCount(0)

        animals = select(a for a in Animal)
        for number, animal in enumerate(animals):
            self.ui.tableWidget.insertRow(number)

            self.ui.tableWidget.setItem(number, 0, QtWidgets.QTableWidgetItem(str(animal.id)))
            self.ui.tableWidget.setItem(number, 1, QtWidgets.QTableWidgetItem(animal.name))
            self.ui.tableWidget.setItem(number, 2, QtWidgets.QTableWidgetItem(animal.description))
            self.ui.tableWidget.setItem(number, 3, QtWidgets.QTableWidgetItem(animal.species.name))
            self.ui.tableWidget.setItem(number, 4, QtWidgets.QTableWidgetItem(animal.state.name))
            self.ui.tableWidget.setItem(number, 5, QtWidgets.QTableWidgetItem(animal.where_now.name))

    @db_session
    def new_animal(self):
        animal = AnimalController(self)
        animal.exec_()

        self.get_animals()

    def edit_animal(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        if len(selection) != 1:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Please select 1 row for editing")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
        else:
            elem = selection[0]
            human = AnimalController(self, int(self.ui.tableWidget.item(elem.row(), 0).text()))
            human.exec_()

            self.get_animals()

    def delete_animal(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        indices = []
        for elem in selection:
            indices.append(int(self.ui.tableWidget.item(elem.row(), 0).text()))

        with db_session:
            delete(a for a in Animal if a.id in indices)

        self.get_animals()

    def select(self):
        selection = self.ui.tableWidget.selectionModel().selectedRows()

        if len(selection) != 1:
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Please select 1 row")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
        else:
            animal = selection[0]
            animal_id = int(self.ui.tableWidget.item(animal.row(), 0).text())
            animal_name = self.ui.tableWidget.item(animal.row(), 1).text()
            self.parent.update_sets(animal_id, animal_name, self.animal_type)
            self.close()
