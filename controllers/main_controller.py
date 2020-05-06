from views.main import *
from views.humans import *

import sys

from enums.species import Species, SpeciesConverter
from enums.state import State, StateConverter
from enums.where_now import WhereNow, WhereNowConverter

from controllers.humans_controller import HumansController
from controllers.client_controller import ClientController
from controllers.animals_controller import AnimalsController

from models import db


class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.setWindowTitle("Shelter")

        db.bind(provider='sqlite', filename='../database/database.sqlite', create_db=True)

        db.provider.converter_classes.append((State, StateConverter))
        db.provider.converter_classes.append((Species, SpeciesConverter))
        db.provider.converter_classes.append((WhereNow, WhereNowConverter))

        db.generate_mapping(create_tables=True)

        self.ui.humans_button.clicked.connect(self.open_humans)
        self.ui.clients_button.clicked.connect(self.open_clients)
        self.ui.animals_button.clicked.connect(self.open_animals)

    def open_humans(self):
        humans = HumansController(self)
        humans.show()

    def open_clients(self):
        client = ClientController(self)
        client.show()

    def open_animals(self):
        animals = AnimalsController(self)
        animals.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainController()

    app.setStyleSheet("QPushButton { padding: 12px; }")

    window.show()
    app.exec_()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys
    sys.excepthook = except_hook
    main()
