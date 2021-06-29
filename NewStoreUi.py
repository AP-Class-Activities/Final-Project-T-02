from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QFormLayout, QFrame, QLineEdit, QSizePolicy,
                             QPushButton, QMessageBox)
from PyQt5.QtCore import Qt
from Store import Store


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        top_label = QLabel('''<h1><i><p style="font-family:Fantasy;color:rgb(59,149,113)">
                              <br><br><br>Create a New Store</p></i></h1>''')
        top_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(top_label)

        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Plain)

        create_button = QPushButton("Create Store")
        create_button.setStyleSheet("background-color:rgb(32,154,26);font: 19px;")
        bottom_spacer = QWidget()
        bottom_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        form_layout = QFormLayout()
        self.name = QLineEdit()
        self.name.setPlaceholderText("must be unique")
        self.name.setStyleSheet("background-color:white;")
        self.owner_name = QLineEdit()
        self.owner_name.setPlaceholderText("store's owner name")
        self.owner_name.setStyleSheet("background-color:white;")
        self.owner_password = QLineEdit()
        self.owner_password.setPlaceholderText("must be 8 characters")
        self.owner_password.setStyleSheet("background-color:white;")
        self.owner_password.setEchoMode(QLineEdit.Password)
        self.owner_password.returnPressed.connect(create_button.click)
        form_layout.addRow("<p>Store Name:</p>", self.name)
        form_layout.addRow("<p>Operator Username:</p>", self.owner_name)
        form_layout.addRow("<p>Operator Password:</p>", self.owner_password)

        create_button.clicked.connect(lambda : self.create_store(self.name.text(), self.owner_name.text(), self.owner_password.text()))

        middle_layout = QVBoxLayout()
        middle_layout.addWidget(hline)
        spacer_label1 = QLabel("<br>")
        middle_layout.addWidget(spacer_label1)
        middle_layout.addLayout(form_layout)
        spacer_label2 = QLabel("<br>")
        middle_layout.addWidget(spacer_label2)
        middle_layout.addWidget(create_button)
        middle_layout.addWidget(bottom_spacer)

        spacer1 = QWidget()
        spacer1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(spacer1, stretch=1)
        bottom_layout.addLayout(middle_layout, stretch=2)
        bottom_layout.addWidget(spacer2, stretch=1)

        main_layout.addLayout(bottom_layout)
    

    def create_store(self, name, owner_name, owner_password):
        try:
            Store(name, owner_name, owner_password)
        except Exception as e:
            error_message = QMessageBox(self)
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle("ERROR")
            error_message.setText(str(e))
            error_message.setStyleSheet("background-color:white")
            error_message.exec()
        finally:
            self.name.setText("")
            self.owner_name.setText("")
            self.owner_password.setText("")

