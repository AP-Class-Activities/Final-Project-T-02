from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QLineEdit, QMessageBox

import sys


class login(QWidget):

    def __init__(self):
        self.setWindowTitle('ورود کاربران')
        self.resize(500, 120)


        layout = QGridlayout()



        label_name = QLabel('نام کاربری')
        self.lineEdit_username = QLineEdit
        self.lineEdit_username.setPlaceholderText('لطفا نام کاربری خود را وارد کنید')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)


        label_password = QLabel('رمز عبور')
        self.lineEdit_password = QLineEdit
        self.lineEdit_password.setPlaceholderText('لطفا رمز عبور خود را وارد کنید')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('جهت ادامه کلیک کنید')

        self.setLayout(layout)

    def check_password(self):
      message = QMessageBox

      if self.lineEdit_password.text() == '' and self.lineEdit_username.text() == '':
        message.setText('')
        message.exec_()

      else:
        message.setText('نام کاربری یا رمز عبور اشتباه است')
        message.exec_()




app = QApplication(sys.argv)
form = login(QWidget)
form.show()
sys.exit(app.exec_())



