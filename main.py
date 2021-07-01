from Store import Store
from MainUi import MainWindow
from PyQt5.QtWidgets import QApplication
import os
import pickle
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


# ------------------------- Database Sample -------------------------
# rmdb()
# store = Store("Central Sports Store", "Ali", "12345678")
# store.seller_sign_up("reza", "rezayi", "12345678", "(4.1,3.1)", "01234567891", "email@gmail.com")
# store.confirm_new_seller(0)
# store.seller_sign_up("hossein", "hassani", "12345678", "(4.1,3.1)", "01234521891", "sdfdfsdf@gmail.com")
# store.confirm_new_seller(0)
# store.seller_sign_up("habib", "merban", "12345678", "(4.1,3.1)", "05688645891", "elsedm@gmail.com")
# store.confirm_new_seller(0)
# seller = store.seller_sign_in("01234567891", "12345678")
# for i in range(18):
#    seller.create_new_product(f"Sample Product {i}", f"This is an explanation fo sample product number {i}. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.")
# for i in range(18):
#    store.confirm_new_product(0)
# store.user_sign_up("morteza", "zia", "(3.2, 2.5)", "12345678", "06813543210", "jtmaifddfsl@yahoo.orga")
# store.user_sign_up("saman", "yekta", "(3.2, 2.5)", "12345678", "04876543210", "gsdfmail@yahoo.orga")
# store.user_sign_up("karim", "alipor", "(3.2, 2.5)", "12345678", "05215643210", "hmasdfil@yahoo.orga")
# seller.add_product_stock(store.products[0], 30000, 13)
# seller.add_product_stock(store.products[1], 10000, 13)
# seller.add_product_stock(store.products[2], 5000, 13)
# user = store.user_sign_in("06813543210", "12345678")
# user.add_comment(store.products[1], "I bought this product and 'tis lit mate, recommend buyin it")
# user.add_comment(store.products[1], "I bought this product and 'tis lit mate, recommend buyin it")
# user.add_comment(store.products[1], "I bought this product and 'tis lit mate, recommend buyin it")
# user.add_comment(store.products[1], "I bought this product and 'tis lit mate, recommend buyin it")
# user.Increase_wallet_balance(80000)
# seller1 = store.seller_sign_in("01234567891", "12345678")
# seller1.create_new_product("Good Product", "hmmmmmmm")
# user.add_product_to_shopping_cart(store.products[0], seller, 1)
# user.add_product_to_shopping_cart(store.products[0], seller, 1)
# user.pay()
# store.seller_sign_up("name", "namepoor", "12345678", "(5.1,1.1)", "02959254447", "salaaljilg@geail.com")
# store.seller_sign_up("farhac", "didebo", "12345678", "(5.5,2.1)", "05489266441", "semaiilg@geail.com")
# seller2 = store.seller_sign_in("05489266441", "12345678")
