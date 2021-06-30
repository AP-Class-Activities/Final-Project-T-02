from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

import sys
from User import User



class login(QWidget):

    def __init__(self, store):
        self.store = store
        self.setWindowTitle('ورود کاربران')
        self.resize(500, 120)


        layout = QGridLayout()



        label_name = QLabel('نام کاربری')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('لطفا نام کاربری خود را وارد کنید')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)


        label_password = QLabel('رمز عبور')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('لطفا رمز عبور خود را وارد کنید')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('جهت ادامه کلیک کنید')
        button_login.clicked.connect(self.check)
        layout.addWidget(2, 0, button_login)

        self.setLayout(layout)

    def check_password(self):
        message = QMessageBox()

        if self.lineEdit_password.text() == User.password and self.lineEdit_username.text() == User.phone_number:
            message.setText('خوش آمدید')
            message.exec_()

        else:
            message.setText('نام کاربری یا رمز عبور اشتباه است')
            message.exec_()







