from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QScrollArea, QTableWidget, QTableWidgetItem, QLabel,
                             QPushButton, QAbstractItemView, QMessageBox, QLineEdit,
                             QFormLayout)
from PyQt5.QtCore import Qt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from datetime import date, timedelta


class MainWidget(QScrollArea):
    def __init__(self, operator):
        super().__init__()
        self.operator = operator

        # to show store's sellers
        sellers_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Sellers&#128070;</p><h3>')
        sellers_label.setAlignment(Qt.AlignCenter)
        self.sellers_table = QTableWidget()
        self.sellers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sellers_table.cellClicked.connect(self.remove_seller)
        self.sellers_table.setColumnCount(4)
        self.fill_sellers_table()

        # to show store's users
        users_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Users&#128070;</p><h3>')
        users_label.setAlignment(Qt.AlignCenter)
        self.users_table = QTableWidget()
        self.users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.users_table.cellClicked.connect(self.remove_user)
        self.users_table.setColumnCount(3)
        self.fill_users_table()

        # to show latest purchases
        purchases_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Purchases&#128070;</p><h3>')
        purchases_label.setAlignment(Qt.AlignCenter)
        self.purchases_table = QTableWidget()
        self.purchases_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.purchases_table.setColumnCount(5)
        self.fill_purchases_table()

        # to show store's products
        products_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Products&#128070;</p><h3>')
        products_label.setAlignment(Qt.AlignCenter)
        self.products_table = QTableWidget()
        self.products_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.products_table.setColumnCount(3)
        self.fill_products_table()

        # to show a graph of store's profits
        profit_graph = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Graph of Last Weeks Profits&#128070;</p><h3>')
        profit_graph.setAlignment(Qt.AlignCenter)
        profit_fig = Figure()
        profit_canvas = FigureCanvasQTAgg(profit_fig)
        profit_canvas.axes = profit_fig.add_subplot()
        profit_canvas.axes.plot([i for i in range(0, -8, -1)],
                                [operator.profit(str(date.today()-timedelta(days=i)),
                                 str(date.today()-timedelta(days=i))) for i in range(8)])

        # to get profits within specific dates
        profit_date_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Get Profits in Specific Periods&#128070;</p><h3>')
        profit_date_label.setAlignment(Qt.AlignCenter)
        start_date = QLineEdit()
        start_date.setPlaceholderText("start date, fomat: YYYY-MM-DD")
        start_date.setStyleSheet("background-color:white;")
        end_date = QLineEdit()
        end_date.setPlaceholderText("end date, fomat: YYYY-MM-DD")
        end_date.setStyleSheet("background-color:white;")
        dates_layout = QHBoxLayout()
        dates_layout.addWidget(start_date)
        dates_layout.addWidget(end_date)
        profit_button = QPushButton("Calculate Profit")
        profit_button.setStyleSheet("background-color:rgb(32,154,26);font: 19px;")

        # to show and confirm pending sellers
        pending_sellers_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Pending Sellers&#128070;</p><h3>')
        pending_sellers_label.setAlignment(Qt.AlignCenter)
        self.pending_sellers_layout = QVBoxLayout()
        self.fill_pending_sellers()

        # to show and confirm pending products
        pending_products_label = QLabel('<h3><p style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Pending Products&#128070;</p><h3>')
        pending_products_label.setAlignment(Qt.AlignCenter)
        self.pending_products_layout = QVBoxLayout()
        self.fill_pending_products()

        # to generate promo codes
        promo_code_label = QLabel('<h3><p&#128070 style="font-family:Fantasy;color:rgb(59,149,113)">&#128070;Generate a Promo Code&#128070;</p><h3>')
        promo_code_label.setAlignment(Qt.AlignCenter)
        promocode_layout = QVBoxLayout()
        promocode_button = QPushButton("Generate Promo Code")
        promocode_button.setStyleSheet("background-color:rgb(32,154,26);font:19px;")
        promocode_form = QFormLayout()
        self.percentage = QLineEdit()
        self.percentage.setPlaceholderText("must be integer")
        self.percentage.setStyleSheet("background-color:white;")
        self.percentage.returnPressed.connect(promocode_button.click)
        self.expiration = QLineEdit()
        self.expiration.setPlaceholderText("# of days, Optional")
        self.expiration.setStyleSheet("background-color:white;")
        self.expiration.returnPressed.connect(promocode_button.click)
        promocode_form.addRow("<p>Percentage:</p>", self.percentage)
        promocode_form.addRow("<p>Expiration:</p>", self.expiration)
        promocode_button.clicked.connect(lambda : self.gen_promocode(int(self.percentage.text()), self.expiration.text()))
        self.promocode_label = QLabel("")
        promocode_layout.addLayout(promocode_form)
        promocode_layout.addWidget(promocode_button)
        promocode_layout.addWidget(self.promocode_label)

        # putting everything together
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.sellers_table)
        left_layout.addWidget(sellers_label)
        left_layout.addWidget(self.purchases_table)
        left_layout.addWidget(purchases_label)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.users_table)
        right_layout.addWidget(users_label)
        right_layout.addWidget(self.products_table)
        right_layout.addWidget(products_label)
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(profit_canvas)
        middle_layout.addWidget(profit_graph)
        middle_layout.addLayout(dates_layout)
        middle_layout.addWidget(profit_button)
        middle_layout.addWidget(profit_date_label)
        middle_layout.addLayout(self.pending_sellers_layout)
        middle_layout.addWidget(pending_sellers_label)
        middle_layout.addLayout(self.pending_products_layout)
        middle_layout.addWidget(pending_products_label)
        middle_layout.addLayout(promocode_layout)
        middle_layout.addWidget(promo_code_label)

        # showing everything in scroll area
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(right_layout)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setWidget(main_widget)


    # Methods

    def fill_sellers_table(self):
        self.sellers = self.operator.sellers
        self.sellers_table.setRowCount(len(self.sellers))
        for row, seller in enumerate(self.sellers):
            self.sellers_table.setItem(row, 0, QTableWidgetItem(seller.name+" "+seller.family))
            self.sellers_table.setItem(row, 1, QTableWidgetItem(seller.email))
            self.sellers_table.setItem(row, 2, QTableWidgetItem(seller.phone))
            self.sellers_table.setItem(row, 3, QTableWidgetItem(str(seller.rating)))


    def remove_seller(self, row, column):
        remove = QMessageBox(self)
        remove.setIcon(QMessageBox.Question)
        remove.setWindowTitle("Warning")
        remove.setText("Do you want to remove this seller?")
        remove.setStyleSheet("background-color:white")        
        remove.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        if remove.exec() == QMessageBox.Yes:
            self.operator.remove_seller(self.sellers[row].seller_id)
            self.fill_sellers_table()  # to update the table


    def fill_users_table(self):
        self.users = self.operator.users
        self.users_table.setRowCount(len(self.users))
        for row, user in enumerate(self.users):
            self.users_table.setItem(row, 0, QTableWidgetItem(user.name+" "+user.lastname))
            self.users_table.setItem(row, 1, QTableWidgetItem(user.email))
            self.users_table.setItem(row, 2, QTableWidgetItem(user.phone_number))


    def remove_user(self, row, column):
        remove = QMessageBox(self)
        remove.setIcon(QMessageBox.Question)
        remove.setWindowTitle("Warning")
        remove.setText("Do you want to remove this user?")
        remove.setStyleSheet("background-color:white")        
        remove.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        if remove.exec() == QMessageBox.Yes:
            self.operator.remove_user(self.users[row]._User__user_id)
            self.fill_users_table()  # to update the table


    def fill_purchases_table(self):
        self.purchases = self.operator.purchases
        self.purchases_table.setRowCount(len(self.purchases[0]))
        for row, purchase in enumerate(self.purchases[0]):
            self.purchases_table.setItem(row, 0, QTableWidgetItem(str(purchase[0])))
            self.purchases_table.setItem(row, 1, QTableWidgetItem(str(purchase[1])))
            self.purchases_table.setItem(row, 2, QTableWidgetItem(str(purchase[2])))
            self.purchases_table.setItem(row, 3, QTableWidgetItem(str(purchase[3])))
            self.purchases_table.setItem(row, 4, QTableWidgetItem(str(purchase[4])))


    def fill_products_table(self):
        self.products = self.operator.products
        self.products_table.setRowCount(len(self.products))
        for row, product in enumerate(self.products):
            self.products_table.setItem(row, 0, QTableWidgetItem(product.name))
            self.products_table.setItem(row, 1, QTableWidgetItem(str(product.least_price)))
            self.products_table.setItem(row, 2, QTableWidgetItem(str(product.sum_stocks)))


    def fill_pending_sellers(self):
        # to empty the list first
        for i in range(self.pending_sellers_layout.count()):
            self.pending_sellers_layout.itemAt(i).widget().setParent(None)
        # to fill the list
        pending_sellers = self.operator.pending_sellers
        for i, seller in enumerate(pending_sellers):
            confirm_button = QPushButton(seller[1])
            confirm_button.setStyleSheet("background-color:rgb(32,154,26);font: 17px;")
            self.pending_sellers_layout.addWidget(confirm_button)
            confirm_button.clicked.connect(lambda : self.confirm_seller(i))

    
    def confirm_seller(self, seller):
        self.operator.confirm_new_seller(seller)
        self.fill_pending_sellers()  # to update pending sellers list
        self.fill_sellers_table()  # to update sellers table


    def fill_pending_products(self):
        # to empty the list first
        for i in range(self.pending_products_layout.count()):
            self.pending_products_layout.itemAt(i).widget().setParent(None)
        # to fill the list
        pending_products = self.operator.pending_products
        for i, product in enumerate(pending_products):
            confirm_button = QPushButton(product[1])
            confirm_button.setStyleSheet("background-color:rgb(32,154,26);font: 17px;")
            self.pending_products_layout.addWidget(confirm_button)
            confirm_button.clicked.connect(lambda : self.confirm_product(i))

    
    def confirm_product(self, product):
        self.operator.confirm_new_product(product)
        self.fill_pending_products()  # to update pending sellers list
        self.fill_products_table()  # to update sellers table


    def gen_promocode(self, percentage, expiration):
        try:
            if expiration:
                code = self.operator.get_promo_code(percentage, int(expiration))
                self.promocode_label.setText(code)
            else:
                code = self.operator.get_promo_code(percentage)
                self.promocode_label.setText(code)
        except Exception as e:
            error_message = QMessageBox(self)
            error_message.setIcon(QMessageBox.Critical)
            error_message.setWindowTitle("ERROR")
            error_message.setText(str(e))
            error_message.setStyleSheet("background-color:white")
            error_message.exec()
        finally:
            self.percentage.setText("")
            self.expiration.setText("")


