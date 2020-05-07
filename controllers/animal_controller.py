from PyQt5.QtWidgets import QMessageBox

from views.animal import *
from pony.orm import *
from models.animal import Animal

from PyQt5 import QtWidgets

from enums.species import Species
from enums.state import State
from enums.where_now import WhereNow


class AnimalController(QtWidgets.QDialog):
    def __init__(self, parent, identifier=None):
        super(AnimalController, self).__init__(parent)
        self.ui = Ui_animal()
        self.ui.setupUi(self)
        self.setWindowTitle("Animal")

        if identifier is not None:
            self.identifier = identifier
            self.is_new = False
            self.init()
        else:
            self.is_new = True

        self.ui.ok_button.clicked.connect(self.ok)

    @db_session
    def init(self):
        animal = Animal[self.identifier]
        self.ui.name_edit.setText(animal.name)
        self.ui.description.setPlainText(animal.description)

        species = animal.species
        state = animal.state
        where_now = animal.where_now

        if species == Species.Cat:
            self.ui.species_combo_box.setCurrentIndex(0)
        elif species == Species.Dog:
            self.ui.species_combo_box.setCurrentIndex(1)

        if state == State.Healthy:
            self.ui.state_combo_box.setCurrentIndex(0)
        elif state == State.Sick:
            self.ui.state_combo_box.setCurrentIndex(1)
        elif state == State.Vaccine_Need:
            self.ui.state_combo_box.setCurrentIndex(2)
        elif state == State.Sick_And_Vaccine_Need:
            self.ui.state_combo_box.setCurrentIndex(3)

        if where_now == WhereNow.Housing:
            self.ui.where_now_combo_box.setCurrentIndex(0)
        elif where_now == WhereNow.Clinic:
            self.ui.where_now_combo_box.setCurrentIndex(1)

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

        species = None
        species_text = self.ui.species_combo_box.currentText()
        if species_text == "Cat":
            species = Species.Cat
        elif species_text == "Dog":
            species = Species.Dog

        state = None
        state_text = self.ui.state_combo_box.currentText()
        if state_text == "Healthy":
            state = State.Healthy
        elif state_text == "Sick":
            state = State.Sick
        elif state_text == "Vaccine need":
            state = State.Vaccine_Need
        elif state_text == "Sick and vaccine need":
            state = State.Sick_And_Vaccine_Need

        where_now = None
        where_now_text = self.ui.where_now_combo_box.currentText()
        if where_now_text == "Housing":
            where_now = WhereNow.Housing
        elif where_now_text == "Clinic":
            where_now = WhereNow.Clinic

        if (species is None) or (state is None) or (where_now is None):
            msg = QMessageBox()

            msg.setWindowTitle("Error")
            msg.setText("Combo box value is not found")
            msg.setStandardButtons(QMessageBox.Ok)

            msg.exec_()
            return

        if self.is_new:
            animal = Animal(name=name,
                            description=self.ui.description.toPlainText(),
                            species=species,
                            state=state,
                            where_now=where_now)
        else:
            animal = Animal[self.identifier]
            animal.name = name
            animal.description = self.ui.description.toPlainText()
            animal.species = species
            animal.state = state
            animal.where_now = where_now

        self.close()
