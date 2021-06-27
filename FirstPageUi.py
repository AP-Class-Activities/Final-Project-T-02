from PyQt5.QtWidgets import (QLabel, QWidget, QFrame, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLineEdit, QSizePolicy)
from PyQt5.QtCore import Qt
import NewStoreUi
import pickle
import time


class MainWidget(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Stores Section
        stores_layout = QVBoxLayout()
        stores_label = QLabel('''<h1><i><p style="font-family:Fantasy;color:rgb(59,149,113)">
                                 <br>Stores List:</p></i></h1>''')
        stores_layout.addWidget(stores_label)
        new_store_button = QPushButton()
        new_store_button.setStyleSheet("background-color:rgb(32,154,26);font: 19px;")
        new_store_button.setText("+")
        new_store_button.clicked.connect(self.__new_store)
        with open("./DATABASE/StoresList.txt", "rt") as stores_file:
            for store in stores_file:
                if store == "\n":
                    continue
                store_button = QPushButton()
                store_button.setStyleSheet("background-color:rgb(32,154,26);font:19px;")
                store_button.setText(store[2:])
                store_button.clicked.connect(lambda : self.__goto_store(store[2:]))
                stores_layout.addWidget(store_button)
            stores_layout.addWidget(new_store_button)
            stores_spacer = QWidget()
            stores_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            stores_layout.addWidget(stores_spacer)
        
        # Operator Section
        operator_layout = QVBoxLayout()
        operator_label = QLabel('''<h1><i><p style="font-family:Fantasy;color:rgb(59,149,113)">
                                 <br>Operator Log-in</p></i></h1>''')
        operator_label.setAlignment(Qt.AlignCenter)
        operator_layout.addWidget(operator_label)
        operator_login_button = QPushButton()
        operator_login_button.setStyleSheet("background-color:rgb(32,154,26);font:19px;")
        operator_login_button.setText("operator login")
        operator_login_button.clicked.connect(lambda : self.__operator_login(operator_name.text(), operator_pass.text()))
        operator_name = QLineEdit()
        operator_name.setStyleSheet("background-color:white;")
        operator_name.returnPressed.connect(operator_login_button.click)
        operator_layout.addWidget(operator_name)
        operator_pass = QLineEdit()
        operator_pass.setStyleSheet("background-color:white;")
        operator_pass.returnPressed.connect(operator_login_button.click)
        operator_pass.setEchoMode(QLineEdit.Password)
        operator_layout.addWidget(operator_pass)
        operator_layout.addWidget(operator_login_button)
        self.operator_login_status = QLabel("")
        self.operator_login_status.setAlignment(Qt.AlignCenter)
        operator_layout.addWidget(self.operator_login_status)
        operator_spacer = QWidget()
        operator_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        operator_layout.addWidget(operator_spacer)


        # Layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addLayout(stores_layout, stretch=2)
        vline = QFrame()
        vline.setFrameShape(QFrame.VLine)
        vline.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(vline)
        main_layout.addLayout(operator_layout)


    # Methods
    def __new_store(self):
        page = NewStoreUi.MainWidget(self.parent)
        self.parent.goto_page(page, [NewStoreUi.MainWidget, self.parent])
    

    def __goto_store(self, store):
        pass


    def __operator_login(self, name, password):
        with open(f"./DATABASE/StoresList.txt", "rt") as stores:
            for store in stores:
                if store == "\n":
                    continue
                with open(f"./DATABASE/{store[2:]}.dat", "rb") as store_file:
                    saved = pickle.load(store_file)
                    if name == saved.owner_name:
                        if password == saved.owner_password:
                            self.operator_login_status.setText('<h4 style="color:green;"><br>success</h4>')
                            time.sleep(1)
                            break
                        self.operator_login_status.setText('<h4 style="color:red;"><br>worong password</h4>')
                        break
            else:
                self.operator_login_status.setText('<h4 style="color:red;"><br>wrong credentials</h4>')


