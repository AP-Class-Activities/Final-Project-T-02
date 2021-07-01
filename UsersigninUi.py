from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

import sys


class user_signin(QWidget):

    def __init__(self, parent, store):
        super().__init__()
        self.store = store
        self.parent = parent

        layout = QGridLayout()

        label1 = QLabel('Name')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('please enter your name')
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        label2 = QLabel('Last Name')
        self.lineEdit_lastname = QLineEdit()
        self.lineEdit_lastname.setPlaceholderText('please enter your last name')
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit_lastname, 1, 1)

        label4 = QLabel('Phone Number')
        self.lineEdit_phonenumber = QLineEdit()
        self.lineEdit_phonenumber.setPlaceholderText('please enter your phone number')
        layout.addWidget(label4, 2, 0)
        layout.addWidget(self.lineEdit_phonenumber, 2, 1)

        label3 = QLabel('Location')
        self.lineEdit_location = QLineEdit()
        self.lineEdit_location.setPlaceholderText('please enter your longitude & latitude: (x, y)')
        layout.addWidget(label3, 3, 0)
        layout.addWidget(self.lineEdit_location, 3, 1)

        label5 = QLabel('E-mail')
        self.lineEdit_email = QLineEdit()
        self.lineEdit_email.setPlaceholderText('please enter your email')
        layout.addWidget(label5, 4, 0)
        layout.addWidget(self.lineEdit_email, 4, 1)

        label_password = QLabel('password')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('please enter your password')
        layout.addWidget(label_password, 5, 0)
        layout.addWidget(self.lineEdit_password, 5, 1)

        label_repeat_password = QLabel('Confirm Password')
        self.lineEdit_repeat_password = QLineEdit()
        self.lineEdit_repeat_password.setPlaceholderText('please re-enter your password')
        self.lineEdit_repeat_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_repeat_password, 6, 0)
        layout.addWidget(self.lineEdit_repeat_password, 6, 1)

        button_login = QPushButton('Click here to Proceed')
        button_login.clicked.connect(self.check)
        layout.addWidget(button_login, 7, 0)

        self.setLayout(layout)

    def check(self):
        try:
            self.store.user_sign_up(self.lineEdit_name.text(), self.lineEdit_lastname.text(),
                                    self.lineEdit_location.text(), self.lineEdit_password.text(),
                                    self.lineEdit_phonenumber.text(), self.lineEdit_email.text())

            self.lineEdit_name.setText("")
            self.lineEdit_lastname.setText("")
            self.lineEdit_password.setText("")
            self.lineEdit_location.setText("")
            self.lineEdit_phonenumber.setText("")
            self.lineEdit_email.setText("")
        except Exception as e:
            message = QMessageBox(self)
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle('Error')
            message.setText(str(e))
            message.setStyleSheet("background-color:white")
            message.exec()




