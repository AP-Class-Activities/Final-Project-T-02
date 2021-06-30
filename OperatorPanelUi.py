from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QScrollArea, QTableWidget, QTableWidgetItem, QLabel,
                             QPushButton, QAbstractItemView, QMessageBox, QLineEdit)
from PyQt5.QtCore import QAbstractProxyModel, Qt
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from datetime import date, timedelta


class MainWidget(QWidget):
    def __init__(self, operator):
        super().__init__()
        self.operator = operator

        self.sellers_table = QTableWidget()
        self.sellers_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sellers_table.cellClicked.connect(self.remove_seller)
        self.sellers_table.setColumnCount(4)
        self.fill_sellers_table()

        self.users_table = QTableWidget()
        self.users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.users_table.cellClicked.connect(self.remove_user)
        self.users_table.setColumnCount(3)
        self.fill_users_table()

        self.purchases_table = QTableWidget()
        self.purchases_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.purchases_table.setColumnCount(5)
        self.fill_purchases_table()

        self.products_table = QTableWidget()
        self.products_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.products_table.setColumnCount(3)
        self.fill_products_table()

        profit_fig = Figure()
        profit_canvas = FigureCanvasQTAgg(profit_fig)
        profit_canvas.axes = profit_fig.add_subplot()
        profit_canvas.axes.plot([i for i in range(0, -8, -1)],
                                [operator.profit(str(date.today()-timedelta(days=i)),
                                 str(date.today()-timedelta(days=i))) for i in range(8)])

        start_date = QLineEdit()
        start_date.setPlaceholderText("start date, fomat: YYYY-MM-DD")
        end_date = QLineEdit()
        end_date.setPlaceholderText("end date, fomat: YYYY-MM-DD")
        dates_layout = QHBoxLayout()
        dates_layout.addWidget(start_date)
        dates_layout.addWidget(end_date)
        profit_button = QPushButton("Calculate Profit")
        profit_button.setStyleSheet("background-color:rgb(32,154,26);font: 16px;")

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.sellers_table)
        left_layout.addWidget(self.purchases_table)
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.users_table)
        right_layout.addWidget(self.products_table)
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(profit_canvas)
        middle_layout.addLayout(dates_layout)
        middle_layout.addWidget(profit_button)

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addLayout(right_layout)
        main_layout.addLayout(middle_layout)
        main_layout.addLayout(left_layout)


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

