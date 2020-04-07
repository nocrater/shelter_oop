from views.human import *
from pony.orm import *
from models import Human


class HumanController(QtWidgets.QDialog):
    def __init__(self, parent, identifier=None):
        super(HumanController, self).__init__(parent)
        self.ui = Ui_human()
        self.ui.setupUi(self)
        self.setWindowTitle("Human")

        if identifier is not None:
            self.identifier = identifier
            self.is_new = False
            self.init()
        else:
            self.is_new = True

        self.ui.ok_button.clicked.connect(self.ok)

    @db_session
    def init(self):
        human = Human[self.identifier]
        self.ui.name_edit.setText(human.name)

    @db_session
    def ok(self):
        if self.is_new:
            Human(name=self.ui.name_edit.text())
        else:
            human = Human[self.identifier]
            human.name = self.ui.name_edit.text()

        self.close()
