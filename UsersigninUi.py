from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

import sys
from User import User
import StoreUi


class user_signin(QWidget):

    def __init__(self, parent, store):
        self.store = store
        self.parent = parent
        self.setWindowTitle('ثبت نام کاربران')
        self.resize(500, 120)


        layout = QGridLayout()



        label1 = QLabel('نام')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('لطفا نام خود را وارد کنید')
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)

        label2 = QLabel('نام خانوادگی')
        self.lineEdit_lastname = QLineEdit()
        self.lineEdit_lastname.setPlaceholderText('لطفا نام خانوادگی خود را وارد کنید')
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit_lastname, 1, 1)

        label4 = QLabel('شماره تماس')
        self.lineEdit_phonenumber = QLineEdit()
        self.lineEdit_phonenumber.setPlaceholderText('لطفا شماره تلفن را وارد کنید')
        layout.addWidget(label4, 2, 0)
        layout.addWidget(self.lineEdit_phonenumber, 2, 1)

        label3 = QLabel('محل سکونت')
        self.lineEdit_city = QLineEdit()
        self.lineEdit_city.setPlaceholderText('لطفا نام استان محل سکونت خود را وارد کنید')
        layout.addWidget(label3, 3, 0)
        layout.addWidget(self.lineEdit_city, 3, 1)


        label_password = QLabel('رمز عبور')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('لطفا رمز عبور خود را وارد کنید')
        layout.addWidget(label_password, 4, 0)
        layout.addWidget(self.lineEdit_password, 4, 1)

        label_repeat_password = QLabel('تکرار رمز عبور')
        self.lineEdit_repeat_password = QLineEdit()
        self.lineEdit_repeat_password.setPlaceholderText('لطفا رمز عبور خود را دوباره وارد کنید')
        layout.addWidget(label_repeat_password, 5, 0)
        layout.addWidget(self.lineEdit_repeat_password, 5, 1)

        button_login = QPushButton('جهت ادامه کلیک کنید')
        button_login.clicked.connect(self.check)
        layout.addWidget(6, 0, button_login)

        self.setLayout(layout)

    def check_phonenumber(self):
        try:
            user = self.store.user_sign_in(self.lineEdit_phonenumber.text() , self.lineEdit_password.text())
            Store_page = StoreUi.MainWidget(self.parent, self.store, user)
            self.parent.goto_page(Store_page, [self.parent, self.store, user])

        except Exception as e:
            message = QMessageBox(self)
            message.setIcon(QMessageBox.critical())
            message.setWindowTitle('این شماره تلفن قبلا استفاده شده است')
            message.setText(str(e))
            message.setStyleSheet("background_color:white")
            message.exec





