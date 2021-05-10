import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt


class Application:
    app = QApplication(sys.argv)
    widget = QWidget()

    def __init__(self):

        styles = """
            QLabel {
                background-color: yellow;
                margin-top: 50px;
            }
        """

        self.app.setStyleSheet(styles)

        duration_label = QLabel(self.widget)
        duration_label.setText('Choose duration: ')
        duration_label.move(10, 10)

        duration = QComboBox(self.widget)
        duration.addItem('40', 40)
        duration.addItem('45', 45)
        duration.addItem('50', 50)
        duration.move(80, 10)

        button1 = QPushButton(self.widget)
        button1.setText('Click')
        button1.move(110, 100)
        button1.clicked.connect(self.button_click)

        self.widget.setWindowTitle('Yooooo')
        self.widget.setGeometry(50, 50, 320, 300)
        self.widget.show()
        sys.exit(self.app.exec_())

    def button_click(self):
        text_label = QLabel(self.widget)
        text_label.setText('Yooo.')
        text_label.move(90, 80)
        text_label.show()


if __name__ == '__main__':
    app = Application()
