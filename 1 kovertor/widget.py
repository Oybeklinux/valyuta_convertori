from PySide6 import QtCore
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget
from konvertor_ui import Ui_Form

class Widget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Konvertor")
        self.setWindowIcon(QIcon("icon.png"))
        self.uzs.textChanged.connect(self.uzs_to_usd)
        self.yopish.clicked.connect(self.yop)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedWidth(400)

    def yop(self):
        self.close()

    def uzs_to_usd(self):
        if self.uzs.text().strip():
            qiymat = float(self.uzs.text())
            usd = round(qiymat / 12400, 1)
            self.usd.setText(str(usd))
        else:
            self.usd.clear()
