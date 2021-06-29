from PyQt5.QtWidgets import (QPushButton, QWidget, QGridLayout, QLabel, QVBoxLayout,
                             QHBoxLayout, QScrollArea, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon


class ProductWidget(QWidget):
    def __init__(self, product, signed_in):
        super().__init__()
        self.setMouseTracking(True)
        self.signed_in = signed_in
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color:rgb(186,217,189)")

        image_label = QLabel()
        image_label.setPixmap(QPixmap(product.image).scaled(180,180))
        name_label = QLabel(f'<p style="font-size:18px">{product.name}</p>')
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.setSpacing(0)

    def enterEvent(self, event):
        self.setStyleSheet("background-color:rgb(171,202,174)")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("background-color:rgb(186,217,189)")
        super().leaveEvent(event)
    
    def mouseReleaseEvent(self, event):
        if self.signed_in:
            pass
        else:
            error_message = QMessageBox(self)
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle("ERROR")
            error_message.setText("You should be signed-in in order to view products!")
            error_message.setStyleSheet("background-color:white")
            error_message.exec()
        super().mouseReleaseEvent(event)



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
        cart_button.clicked.connect(lambda : self.open_cart(self.user))
        bar_layout.addWidget(cart_button, stretch=1)
        spacer = QLabel('')
        bar_layout.addWidget(spacer, stretch=9)

        if user:
            welcome_label = QLabel(f"Welcome {user.name}!")
            bar_layout.addWidget(welcome_label, stretch=7)
            quit_button = QPushButton("Log Out of Account")
            bar_layout.addWidget(quit_button, stretch=3)
        else:
            sign_in_button = QPushButton("\nSign-in\n")
            sign_in_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(sign_in_button, stretch=1)

            sign_up_button = QPushButton("\nSign-up\n")
            sign_up_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(sign_up_button, stretch=1)


        products_widget = QWidget()
        products_layout = QGridLayout()
        products_widget.setLayout(products_layout)
        for i, product in enumerate(store.products):
            product_widget = ProductWidget(product, bool(user))
            products_layout.addWidget(product_widget, i//4, i%4)
        scroll = QScrollArea()
        scroll.setWidget(products_widget)

        main_layout = QVBoxLayout()
        main_layout.addLayout(bar_layout)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    
    def open_cart(self, user):
        if not user:
            error_message = QMessageBox(self)
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle("ERROR")
            error_message.setText("You are NOT signed-in!")
            error_message.setStyleSheet("background-color:white")
            error_message.exec()
        else:
            pass

