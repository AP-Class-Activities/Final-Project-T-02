'''

Email: anita.karimi.17@gmail.com

'''

import pickle
import os
import datetime
from Product import Product
from Seller import Seller


class User:
     def __init__(self,store, name, lastname, location, password, phone_number, email):
         self.__store = store
         self.__name = name
         self.__lastname = lastname
         self.__location = location
         self.__password = password
         self.__phone_number = phone_number
         self.__email = email
         self.__shopping_cart = {}
         self.__balance = 0
         self.__purchases = []
         self.__user_id = self.__gen_user_id()
         self.__save()

         with open(f"./DATABASE/{self.__store.name}/Users/UsersList.txt", "at") as users:
             users.write("\n" + self.__user_id)


   #Methods

     def __gen_user_id(self):
         try:
             with open(f"./DATABASE/{self.__store.name}/Users/UsersList.txt", "rt") as user:
                 for line in user:
                     pass
                 last_user_id = int(line[2:].strip("\n"))
         except UnboundLocalError:
             last_user_id = 0  # in case there are no users yet

         return "US" + (6 - len(str(last_user_id+1))) * "0" + str(last_user_id+1)

     def __save(self):
         with open(f"./DATABASE/{self.__store.name}/Users/{self.__user_id}.dat","wb") as dat_file:
             pickle.dump(self, dat_file)


     #Increase the wallet balance

     def Increase_wallet_balance(self, addition):
         if addition>0:
             self.__balance += addition
             self.__save()



     #Add a product from the store to the shopping cart

     def add_product_to_shopping_cart(self, product, seller, number):
         self.__shopping_cart[product] = [seller, number]
         product.decrease_stock(seller, number)
         self.__save()


     def remove_product_from_shopping_cart(self, product):
         for user_product in list(self.__shopping_cart.keys()):
             if user_product.product_id == product.product_id:
                 user_product.decrease_stock(self.__shopping_cart[user_product][0], -self.__shopping_cart[user_product][1])
                 del self.__shopping_cart[user_product]
                 self.__save()
                 break
         else:
             raise ValueError("no such product in shopping cart")


     #Pay for shopping cart products

     def pay(self):
         sum = 0
         purchase = []
         for product, seller_number in self.__shopping_cart.items():
              sum += product.price(seller_number[0]) * seller_number[1]
              purchase.append([datetime.date.today(), self.__name+" "+self.__lastname, product.name,
                               product.price(seller_number[0]), seller_number[1], seller_number[0].seller_id])
         if self.__balance >= sum:
             self.__balance -= sum
             self.__purchases.append(purchase)
             self.__store.add_purchase(purchase)
             self.__shopping_cart = {}
             self.__save()
             return True
         else:
             return False


     #Add a new comments

     def add_comment(self, product, comment):
         if not isinstance(comment, str):
             raise ValueError("comment must be a string")
         product.add_comment(self.__name+" "+self.__lastname, comment)

     def add_rating(self, seller, rating):
         if not (0 <= rating <= 5):
             raise ValueError("ratings can only be from 1 to 5")
         seller.rating(rating)


     #setters and getters

     @property
     def name(self):
              return self.__name
     @name.setter
     def name(self, value):
              self.__name = value
              self.__save()

     @property
     def lastname(self):
              return self.__lastname
     @lastname.setter
     def lastname(self, value):
              self.__lastname = value
              self.__save()

     @property
     def location(self):
              return self.__location
     @location.setter
     def location(self, value):
              self.__location = value
              self.__save()

     @property
     def password(self):
              return self.__password
     @password.setter
     def password(self, value):
              if len(self.__password) < 8:
                     raise ValueError("the password should be more than (8) Characters")
              self.__password = value
              self.__save()

     @property
     def phone_number(self):
              return self.__phone_number
     @phone_number.setter
     def phone_number(self, value):
              if len(self.__phone_number) != 11:
                    raise ValueError("Phone number must have (11) digits")
              self.__phone_number = value
              self.__save()

     @property
     def email(self):
              return self.__email
     @email.setter
     def email(self, value):
              self.__email = value
              self.__save()

     @property
     def shopping_cart(self):
         return self.__shopping_cart

     @property
     def balance(self):
         return self.__balance


