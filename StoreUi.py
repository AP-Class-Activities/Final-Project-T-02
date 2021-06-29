from PyQt5.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout, QLabel,
                             QVBoxLayout, QHBoxLayout, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import os
import pickle


class MainWidget(QWidget):
    def __init__(self, parent, store, user=None):
        super().__init__()
        self.parent = parent
        self.user = user

        bar_layout = QHBoxLayout()
        cart_pic = QPixmap("./DATABASE/Icons/cart.png")
        cart_button = QPushButton()
        cart_button.setIcon(QIcon(cart_pic))
        cart_button.setIconSize(cart_pic.rect().size()/7)
        # cart_button.setStyleSheet("border-radius: 900px;")
        bar_layout.addWidget(cart_button, stretch=1)
        spacer = QLabel('')
        bar_layout.addWidget(spacer, stretch=9)

        if user:
            welcome_label = QLabel(f"Welcome {user.name}!")
            bar_layout.addWidget(welcome_label, stretch=7)
            quit_button = QPushButton("Log Out of Account")
            bar_layout.addWidget(quit_button, stretch=3)
        else:
            sign_in_button = QPushButton("Sign-in")
            bar_layout.addWidget(sign_in_button, stretch=1)

            sign_up_button = QPushButton("Sign-up")
            bar_layout.addWidget(sign_up_button, stretch=1)


        products_widget = QWidget()
        products_layout = QGridLayout()
        products_widget.setLayout(products_layout)
        for pic, i in enumerate(os.listdir("./DATABASE/Central Sports Store/Products/")):
            if i == "ProductsList.txt":
                continue
            with open(f"./DATABASE/Central Sports Store/Products/{i}", "rb") as f:
                pro = pickle.load(f)
                image_label = QLabel()
                image_label.setPixmap(QPixmap(pro.image).scaled(180,180))
                name_label = QLabel(pro.name)
                name_label.setAlignment(Qt.AlignCenter)
                pro_layout = QVBoxLayout()
                pro_layout.addWidget(image_label, stretch=7)
                pro_layout.addWidget(name_label, stretch=7)
                products_layout.addLayout(pro_layout, pic//4, pic%4)
        scroll = QScrollArea()
        # scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setWidget(products_widget)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(bar_layout)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)


app = QApplication([])
win = MainWidget(None, None)
win.show()
app.exec()
