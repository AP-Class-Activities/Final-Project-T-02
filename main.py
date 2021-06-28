from Store import Store
from MainUi import MainWindow
from PyQt5.QtWidgets import QApplication
import os
from shutil import rmtree


def rmdb():
    '''Deletes Database
       Usefull for Testing
       Use with Caution'''

    for file in os.listdir("./DATABASE/"):
        if file == "Icons":
            continue
        try:
            rmtree(f"./DATABASE/{file}")
        except:
            os.remove(f"./DATABASE/{file}")
    with open("./DATABASE/StoresList.txt", "wt") as file:
        pass


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()

