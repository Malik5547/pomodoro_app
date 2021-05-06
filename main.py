import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    text_label = QLabel(widget)
    text_label.setText('Yooo.')
    text_label.move(110, 80)

    widget.setGeometry(50, 50, 320, 300)
    widget.setWindowTitle('Yooooo')
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
