from PyQt6.QtCore import pyqtSlot, QThread
from PyQt6.QtWidgets import QTabWidget, QGridLayout, QLabel, QLineEdit, QPushButton


class CentralWidget(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.data = QLineEdit(self)

        self.button = QPushButton("Speichern")
        self.button.pressed.connect(self.handel)

        layout = QGridLayout(self)
        self.setLayout(layout)

        layout.addWidget(QLabel("Daten"), 1, 1)
        layout.addWidget(self.data, 1, 2)
        layout.addWidget(self.button, 2, 1, 1, 2)

    @pyqtSlot()
    def handel(self):
        print("Baue Verbinung auf.")
        QThread.sleep(5)
        print("Verbinung aufgebaut.")

        # Aufgabe:
        # Erstellen Sie eine QThread, welcher parallel zu unserer GUI läuft.
