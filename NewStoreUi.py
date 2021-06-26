from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        lbl = QLabel("soon")
        lout = QVBoxLayout()
        lout.addWidget(lbl)
        self.setLayout(lout)

