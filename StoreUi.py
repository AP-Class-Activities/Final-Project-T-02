from PyQt5.QtWidgets import (QPushButton, QWidget, QGridLayout, QLabel, QVBoxLayout,
                             QHBoxLayout, QScrollArea, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import ProductUi, CartUi
from sellersigninUi import selelr_signin
from sellerloginUi import seller_login
from UsersigninUi import user_signin
from UserloginUi import login


class ProductWidget(QWidget):
    def __init__(self, parent, product, user):
        super().__init__()
        self.parent = parent
        self.product = product
        self.user = user
        self.setMouseTracking(True)
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
        if self.user:
            page = ProductUi.MainWidget(self.product, self.user)
            self.parent.goto_page(page, [ProductUi.MainWidget, self.product, self.user])
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
        self.store = store
        self.user = user
        self.parent.change_toolbar_title(store.name)

        bar_layout = QHBoxLayout()
        cart_pic = QPixmap("./DATABASE/Icons/cart.png")
        cart_button = QPushButton()
        cart_button.setIcon(QIcon(cart_pic))
        cart_button.setIconSize(cart_pic.rect().size()/7)
        cart_button.clicked.connect(self.open_cart)
        bar_layout.addWidget(cart_button, stretch=1)
        spacer = QLabel('')
        bar_layout.addWidget(spacer, stretch=9)

        if user:
            welcome_label = QLabel(f'<b><p style="color:green;">Welcome {user.name}!</p><b>')
            bar_layout.addWidget(welcome_label, stretch=7)
            quit_button = QPushButton("Log Out of Account")
            quit_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(quit_button, stretch=3)
            quit_button.clicked.connect(self.quit)
        else:
            seller_sign_in_button = QPushButton("Sellers\nSign-in")
            seller_sign_in_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(seller_sign_in_button, stretch=1)
            seller_sign_in_button.clicked.connect(self.seller_sign_in)

            seller_sign_up_button = QPushButton("Sellers\nSign-up")
            seller_sign_up_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(seller_sign_up_button, stretch=1)
            seller_sign_up_button.clicked.connect(self.seller_sign_up)

            user_sign_in_button = QPushButton("Users\nSign-in")
            user_sign_in_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(user_sign_in_button, stretch=1)
            user_sign_in_button.clicked.connect(self.user_sign_in)

            user_sign_up_button = QPushButton("Users\nSign-up")
            user_sign_up_button.setStyleSheet("background-color:rgb(32,154,26);font:17px;")
            bar_layout.addWidget(user_sign_up_button, stretch=1)
            user_sign_up_button.clicked.connect(self.user_sign_up)


        products_widget = QWidget()
        products_layout = QGridLayout()
        products_widget.setLayout(products_layout)
        for i, product in enumerate(store.products):
            product_widget = ProductWidget(parent, product, user)
            products_layout.addWidget(product_widget, i//6, i%6)
        scroll = QScrollArea()
        scroll.setWidget(products_widget)

        main_layout = QVBoxLayout()
        main_layout.addLayout(bar_layout)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

    
    def open_cart(self):
        if not self.user:
            error_message = QMessageBox(self)
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle("ERROR")
            error_message.setText("You are NOT signed-in!")
            error_message.setStyleSheet("background-color:white")
            error_message.exec()
        else:
            page = CartUi.MainWidget(self.store, self.user)
            self.parent.goto_page(page, [CartUi.MainWidget, self.store, self.user])


    def quit(self):
        self.parent.go_home()


    def seller_sign_in(self):
        page = seller_login(self.parent, self.store)
        self.parent.goto_page(page, [seller_login, self.parent, self.store])


    def seller_sign_up(self):
        page = selelr_signin(self.parent, self.store)
        self.parent.goto_page(page, [selelr_signin, self.parent, self.store])
    

    def user_sign_in(self):
        page = login(self.parent, self.store)
        self.parent.goto_page(page, [login, self.parent, self.store])

    
    def user_sign_up(self):
        page = user_signin(self.parent, self.store)
        self.parent.goto_page(page, [user_signin, self.parent, self.store])

