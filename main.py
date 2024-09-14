import sys
from interface import MyWidget
from PySide6 import QtCore, QtWidgets, QtGui


def main():
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
