from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar,
                             QStackedLayout, QWidget, QLabel, QAction,
                             QSizePolicy)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.resize(400, 400)


        # Toolbar
        Toolbar = QToolBar()
        Toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        Toolbar.setIconSize(QSize(Toolbar.iconSize().width()*2, Toolbar.iconSize().height()*2))
        
        BackAction = QAction(QIcon("./DATABASE/Icons/Back.png"), "Go Back", self)
        BackAction.triggered.connect(self.__GoBack)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        ToolbarTitle = QLabel('<b><p style="color:green;">Welcome to Market</p></b>')

        HomeAction = QAction(QIcon("./DATABASE/Icons/Home.png"), "Home Page", self)
        HomeAction.triggered.connect(self.__GoHome)

        Toolbar.addAction(BackAction)
        Toolbar.addWidget(spacer)
        Toolbar.addWidget(ToolbarTitle)
        Toolbar.addWidget(spacer2)
        Toolbar.addAction(HomeAction)
        self.addToolBar(Toolbar)


        # Layout
        self.Layout = QStackedLayout()
        CentralWidget = QWidget()
        CentralWidget.setLayout(self.Layout)
        self.setCentralWidget = CentralWidget


    # Methods
    def __GoBack(self):
        self.Layout.setCurrentIndex(self.Layout.currentIndex()-1)
    
    def __GoHome(self):
        self.Layout.setCurrentIndex(0)

