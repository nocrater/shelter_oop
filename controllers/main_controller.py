from views.main import *
import sys


class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainForm()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
