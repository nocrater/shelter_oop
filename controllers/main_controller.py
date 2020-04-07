from views.main import *
from views.humans import *
import sys
from controllers.humans_controller import HumansController
from models import db


class MainController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.setWindowTitle("Shelter")

        db.bind(provider='sqlite', filename='../database/database.sqlite', create_db=True)
        db.generate_mapping(create_tables=True)

        self.ui.humans_button.clicked.connect(self.open_humans)

    def open_humans(self):
        humans = HumansController(self)
        humans.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainController()

    app.setStyleSheet("QPushButton { padding: 12px; }")

    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
