from PyQt5.QtWidgets import (QMainWindow, QToolBar, QStackedLayout,
                             QWidget, QLabel, QAction, QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
import FirstPageUi


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Market")
        self.showMaximized()

        # Toolbar
        toolbar = QToolBar()
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        toolbar.setIconSize(QSize(toolbar.iconSize().width()*2, toolbar.iconSize().height()*2))
        
        back_action = QAction(QIcon("./DATABASE/Icons/Back.png"), "Go Back", self)
        back_action.triggered.connect(self.__go_back)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.toolbar_title = QLabel('<b><p style="color:green;">Welcome to Market</p></b>')

        home_action = QAction(QIcon("./DATABASE/Icons/Home.png"), "Home Page", self)
        home_action.triggered.connect(self.go_home)

        toolbar.addAction(back_action)
        toolbar.addWidget(spacer)
        toolbar.addWidget(self.toolbar_title)
        toolbar.addWidget(spacer2)
        toolbar.addAction(home_action)
        self.addToolBar(toolbar)


        # Layout
        self.layout = QStackedLayout()
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color:rgb(206,242,210);")
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)


        # Page Setup
        self.page_args = {0: [FirstPageUi.MainWidget, self]}
        first_page = FirstPageUi.MainWidget(self)
        self.layout.addWidget(first_page)



    # Methods
    def change_toolbar_title(self, title):
        self.toolbar_title.setText(f'<b><p style="color:green;">{title}</p></b>')


    def __go_back(self):
        current_index = self.layout.currentIndex()
        if current_index > 0:
            page = self.page_args[current_index-1][0](*self.page_args[current_index-1][1:])
            self.layout.removeWidget(self.layout.widget(current_index))
            self.layout.insertWidget(current_index-1, page)
            self.layout.setCurrentIndex(current_index-1)
            if self.layout.currentIndex() == 0:
                self.change_toolbar_title("Welcome to Market")


    def go_home(self):
        while self.layout.currentIndex() > 0:
            self.__go_back()


    def goto_page(self, page, args):
        for _ in range(self.layout.currentIndex()+1, self.layout.count()):
            self.layout.removeWidget(self.layout.widget(_))
        self.layout.setCurrentIndex(self.layout.addWidget(page))
        self.page_args[self.layout.indexOf(page)] = args

