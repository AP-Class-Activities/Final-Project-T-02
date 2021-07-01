from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

import sys
import StoreUi



class login(QWidget):

    def __init__(self, parent, store):
        super().__init__()
        self.store = store
        self.parent = parent


        layout = QGridLayout()



        label_phone = QLabel('Phone Number')
        self.lineEdit_phone = QLineEdit()
        self.lineEdit_phone.setPlaceholderText('please enter your phone number')
        layout.addWidget(label_phone, 0, 0)
        layout.addWidget(self.lineEdit_phone, 0, 1)


        label_password = QLabel('Password')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('please enter your password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Click here to Proceed')
        button_login.clicked.connect(self.check)
        layout.addWidget(button_login, 2, 0)

        self.setLayout(layout)

    def check(self):
        user = self.store.user_sign_in(self.lineEdit_phone.text(), self.lineEdit_password.text())
        if user:
            Store_page = StoreUi.MainWidget(self.parent, self.store, user)
            self.parent.goto_page(Store_page, [StoreUi.MainWidget, self.parent, self.store, user])

        else:
            message = QMessageBox(self)
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle('Error')
            message.setText('Wrong Credentials')
            message.setStyleSheet('background-color:white')
            message.exec()






