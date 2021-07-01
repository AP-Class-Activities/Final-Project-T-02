from os import spawnlp
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                             QComboBox, QSpinBox, QScrollArea, QSizePolicy, QPlainTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class MainWidget(QScrollArea):
    def __init__(self, product, user):
        super().__init__()
        self.product = product
        self.user = user
        self.product_sellers = product.sellers

        image = QLabel()
        image.setPixmap(QPixmap(product.image).scaled(350,350))

        name = QLabel(f'<h1 syle="font-family:Fantasy;color:rgb(59,149,113)">product.name</h1>')
        name.setAlignment(Qt.AlignCenter)

        explanation = QLabel(product.explanation)
        explanation.setAlignment(Qt.AlignCenter)
        explanation.setWordWrap(True)

        self.price = QLabel(f'<strong style="font-size:24;font-family:Fantasy;color:rgb(59,149,113)"><i>${str(product.least_price)}$</i></strong>')
        self.price.setAlignment(Qt.AlignCenter)

        self.sellers = QComboBox()
        self.sellers.setStyleSheet("font-size:18px;")
        first_seller = 0
        for i, seller in enumerate(self.product_sellers):  # filling sellers combobox
            if product.price(seller) == product.least_price:
                first_seller = i
            self.sellers.addItem(f"{seller.name} {seller.family}, ${product.price(seller)}, #{product.stock(seller)}")
        self.sellers.setCurrentIndex(first_seller)  # to choose cheapest price by default
        self.sellers.currentIndexChanged.connect(lambda : self.price_changed)

        # number of products that user wants to buy
        self.number = QSpinBox()
        self.number.setMinimum(1)
        self.number.valueChanged.connect(self.price_changed)

        add_to_cart_button = QPushButton("\nAdd Product to Shopping Cart\n")
        add_to_cart_button.setStyleSheet("background-color:rgb(32,154,26);font:21px;font-weight:bold;")
        add_to_cart_button.clicked.connect(self.add_to_cart)
        cart_layout = QHBoxLayout()
        cart_spacer1 = QWidget()
        cart_spacer1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        cart_spacer2 = QWidget()
        cart_spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        cart_layout.addWidget(cart_spacer1, stretch=1)
        cart_layout.addWidget(add_to_cart_button, stretch=4)
        cart_layout.addWidget(cart_spacer2, stretch=1)


        self.comments = QVBoxLayout()
        self.fill_comments()

        # to add a new comment
        new_comment_layout = QHBoxLayout()
        self.new_comment = QPlainTextEdit()
        self.new_comment.setPlaceholderText("Write your comment here...")
        self.new_comment.setStyleSheet("background-color:white")
        comment_button = QPushButton("Add comment...")
        comment_button.setStyleSheet("background-color:rgb(32,154,26);font-size:16px;")
        comment_button.clicked.connect(lambda : self.send_comment(self.new_comment.toPlainText()))
        new_comment_layout.addWidget(self.new_comment, stretch=10)
        new_comment_layout.addWidget(comment_button, stretch=1)
        comments_layout = QVBoxLayout()
        comments_layout.setSpacing(10)
        comments_layout.addLayout(self.comments)
        comments_layout.addLayout(new_comment_layout)

        # putting everything together
        left_layout = QVBoxLayout()
        left_layout.setSpacing(30)
        left_layout.addWidget(image)
        left_layout.addWidget(name)
        left_layout.addWidget(self.price)
        right_layout = QVBoxLayout()
        right_layout.setSpacing(30)
        right_layout.addWidget(explanation)
        right_layout.addWidget(self.sellers)
        right_layout.addWidget(self.number)
        top_layout = QHBoxLayout()
        top_layout.setSpacing(260)
        top_layout.addLayout(left_layout)
        top_layout.addLayout(right_layout)
        spacer1 = QWidget()
        spacer1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(spacer1, stretch=1)
        bottom_layout.addLayout(comments_layout, stretch=2)
        bottom_layout.addWidget(spacer2, stretch=1)
        main_layout = QVBoxLayout()
        main_layout.setSpacing(100)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(cart_layout)
        main_layout.addLayout(bottom_layout)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setWidget(main_widget)


    def price_changed(self):
        text = self.sellers.currentText()
        ds = text.find("$")+1
        p = int(text[ds:ds+(text[ds:].find(","))]) * self.number.value()
        self.price.setText(f'<strong style="font-family:Fantasy;color:rgb(59,149,113)"><i>${p}$</i></strong>')


    def add_to_cart(self):
        self.user.add_product_to_shopping_cart(self.product, self.product_sellers[self.sellers.currentIndex])


    def fill_comments(self):
        for i in range(self.comments.count()):  # to empty the list first
            self.comments.itemAt(i).widget().setParent(None)
        for comment in self.product.comments:  # to fill the comment section
            comment_label = QLabel(f'<h3><i>{comment[0]}: </i></h3><p styel="font-size:16px;">{comment[1]}</p>')
            comment_label.setWordWrap(True)
            comment_label.setStyleSheet("border: 3px solid green;")
            self.comments.addWidget(comment_label)



    def send_comment(self, comment):
        self.product.add_comment(self.user.name+" "+self.user.lastname, comment)
        comment_label = QLabel(f'<h3><i>{self.user.name+" "+self.user.lastname}: </i></h3><p styel="font-size:16px;">{comment}</p>')
        comment_label.setWordWrap(True)
        comment_label.setStyleSheet("border: 3px solid green;")
        self.comments.addWidget(comment_label)
        self.new_comment.clear()

