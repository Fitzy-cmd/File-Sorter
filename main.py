from gui import *
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = GUI()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
