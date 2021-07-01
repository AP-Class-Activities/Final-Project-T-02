from PyQt5.QtWidgets import (QScrollArea, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QPushButton, QLineEdit, QMessageBox, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap



class ProductWidget(QWidget):
    def __init__(self, product, price, number, user):
        super().__init__()
        self.product = product
        self.user = user
        self.setMouseTracking(True)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.setStyleSheet("background-color:rgb(186,217,189)")

        image_label = QLabel()
        image_label.setPixmap(QPixmap(product.image).scaled(180,180))
        name_label = QLabel(f'<p style="font-size:18px">{product.name}</p>')
        number_label = QLabel(f'<p style="font-size:18px">number: {number}</p>')
        price_label = QLabel(f'<p style="font-size:18px">{price}</p>')
        layout.addWidget(image_label)
        layout.addWidget(name_label)
        layout.addWidget(number_label)
        layout.addWidget(price_label)


    def enterEvent(self, event):
        self.setStyleSheet("background-color:rgb(171,202,174)")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("background-color:rgb(186,217,189)")
        super().leaveEvent(event)
    
    def mouseReleaseEvent(self, event):
        message = QMessageBox(self)
        message.setIcon(QMessageBox.Question)
        message.setWindowTitle("Remove")
        message.setText("Do you really want to remove this product from your shopping cart?")
        message.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        message.setStyleSheet("background-color:white")
        if message.exec() == QMessageBox.Yes:
            self.user.remove_product_from_shopping_cart(self.product)
        super().mouseReleaseEvent(event)


class MainWidget(QScrollArea):
    def __init__(self, store, user):
        super().__init__()
        self.store = store
        self.user = user

        balance_layout = QVBoxLayout()
        balance_layout.addSpacing(10)
        balance_title = QLabel('<h2 style="font-family:Fantasy;color:rgb(59,149,113)"><i>Balance</i></h2>')
        self.balance = QLabel(f'<h2 style="font-family:Fantasy">Your Current Balance is: {user.balance}</h3>')
        self.increase_balance_amount = QLineEdit()
        self.increase_balance_amount.setPlaceholderText("enter amount")
        balance_button = QPushButton("Increase Balance")
        balance_button.setStyleSheet("background-color:rgb(32,154,26);font:18px;")
        balance_button.clicked.connect(self.increase_balance)
        self.balance_result = QLabel("")
        self.balance_result.setAlignment(Qt.AlignCenter)
        balance_layout.addWidget(balance_title)
        balance_layout.addWidget(self.balance)
        balance_layout.addWidget(self.increase_balance_amount)
        balance_layout.addWidget(balance_button)
        balance_layout.addWidget(self.balance_result)


        self.sum_prices = 0
        self.bargain = 0

        products_layout = QVBoxLayout()
        products_layout.addSpacing(10)
        for product, s_n in user.shopping_cart.items():
            product_widget = ProductWidget(product, product.price(s_n[0]), s_n[1], user)
            products_layout.addWidget(product_widget)
            self.sum_prices += product.price(s_n[0])

        self.total_label = QLabel(f"<b>total: {self.sum_prices}</b>")
        products_layout.addWidget(self.total_label)

        promocode_layout = QVBoxLayout()
        promocode_layout.addSpacing(10)
        promocode_title = QLabel('<h2 style="font-family:Fantasy;color:rgb(59,149,113)"><i>Use a Promo Code</i></h2>')
        promocode_title.setAlignment(Qt.AlignCenter)
        self.promocode = QLineEdit()
        self.promocode.setPlaceholderText("enter promo code")
        promocode_button = QPushButton("Check")
        promocode_button.setStyleSheet("background-color:rgb(32,154,26);font:18px;")
        promocode_button.clicked.connect(self.check_promocode)
        self.promocode_result = QLabel("")
        self.promocode_result.setAlignment(Qt.AlignCenter)
        promocode_layout.addWidget(promocode_title)
        promocode_layout.addWidget(self.promocode)
        promocode_layout.addWidget(promocode_button)
        promocode_layout.addWidget(self.promocode_result)



        pay_button = QPushButton("Pay and Buy products")
        pay_button.setStyleSheet("background-color:rgb(32,154,26);font:21px;font-weight:bold;")
        pay_button.clicked.connect(self.pay)
        self.pay_result = QLabel("")
        products_layout.addWidget(pay_button)
        products_layout.addWidget(self.pay_result)

        main_layout = QHBoxLayout()
        main_layout.setSpacing(60)
        main_layout.addLayout(promocode_layout)
        main_layout.addLayout(products_layout)
        main_layout.addLayout(balance_layout)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setWidget(main_widget)

    def check_promocode(self):
        for code, data in self.store.promo_codes.items():
            if self.promocode.text() == code:
                self.promocode_result.setText('<h3 style="font-family:Fantasy;color:rgb(59,149,113)">Promo Code Successfully Added!</h3>')
                self.total_label.setText(f"<b>total: {self.sum_prices*data[1]//100}</b>")
                self.sum_prices, self.bargain = self.sum_prices*data[1]//100, self.sum_prices-self.sum_prices*data[1]//100
                break
        else:
            self.promocode_result.setText('<h3 style="font-family:Fantasy;color:red">Wrong Promo Code!</h3>')
    


    def increase_balance(self):
        self.user.Increase_wallet_balance(int(self.increase_balance_amount.text()))
        self.balance.setText(f'<h2 style="font-family:Fantasy">Your Current Balance is: {self.user.balance}</h3>')
        self.balance_result.setText('<h3 style="font-family:Fantasy;color:rgb(59,149,113)">Success!</h3>')


    def pay(self):
        self.user.pay()
        self.user.Increase_wallet_balance(self.bargain)
        self.balance.setText(f'<h2 style="font-family:Fantasy">Your Current Balance is: {self.user.balance}</h3>')
        self.pay_result.setText('<h3 style="font-family:Fantasy;color:rgb(59,149,113)">Success!</h3>')

