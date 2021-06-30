from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

import sys
from Seller import Seller
import StoreUi



class seller_login(QWidget):

    def __init__(self, parent, store):
        self.store = store
        self.parent = parent
        self.setWindowTitle('ورود فروشندگان')
        self.resize(500, 120)


        layout = QGridlLayout()



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

    def check(self):
        try:
            user = self.store.Seller_sign_in(self.lineEdit_phonenumber.text(), self.lineEdit_password.text())
            Store_page = StoreUi.MainWidget(self.parent, self.store, Seller)
            self.parent.goto_page(Store_page, [self.parent, self.store, Seller])

        except Exception as e:
            message = QMessageBox(self)
            message.setIcon(QMessageBox.critical())
            message.setWindowTitle('نام کاربری یا رمز عبور اشتباه است')
            message.setText(str(e))
            message.setStyleSheet("background_color:white")
            message.exec




