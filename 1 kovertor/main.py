from PySide6.QtWidgets import QApplication, QWidget
from widget import Widget
app = QApplication()

widget = Widget()
widget.show()


print("")
app.exec()