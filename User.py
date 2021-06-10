'''

Email: anita.karimi.17@gmail.com

'''

import pickle
import os
import random
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
         self.__shopping_cart = []
         self.__balance = 0
         self.__save()



     #directories

     os.mkdir(f"./DATABASE/{self.__name }/Users")
     os.mkdir(f"./DATABASE/{self.__name}/Products")
     os.mkdir(f"./DATABASE/{self.__name}/Sellers")


   #Methods


     #user sign-in

     def user_sign_in(self, username, password):
        self.__load()
        for user in self.__Users:
            if user.username == username and user.password == password:
                return True
            else:
                return False


    # loading users

     with open(f"./DATABASE/{self.__name}/Users/UsersList.txt", "rt") as users_list:
         for line in users_list:
             if line != "\n":
                 with open(f"./DATABASE/{self.__name}/Users/{line}.dat", "rb") as user:
                     self.__users.append(pickle.load(user))

     #Increase the wallet balance

     def Increase_wallet_balance(self, addition):
         addition = 0
         if addition>0:
             user.__balance += addition



     #Add a product from the store to the shopping cart

     def add_product_to_shopping_cart(self, product, seller, number):
         sellers_list = product.sellers
         self.__shopping_cart.append(product.sellers(seller.name)
         product.decrease_stock(seller, number)

     #Pay for shopping cart products

     def pay(self,number, product, seller):
         sum = 0
         for product in self.__shopping_cart:
              sum += (product.price(seller.name) * number
         if self.__balance > sum:
              return True


     #Add a new comments

     def add_comment(self, sender, comment):
         if not isinstance(comment, str):
             raise ValueError("comment must be a string")
         self.__comments.append([sender, comment])
         self.__save()


     #setters and getters

     @property
     def name(self):
              return self.__name
     @name.setter
     def name(self, value):
              self.__name = value

     @property
     def lastname(self):
              return self.__lastname
     @lastname.setter
     def lastname(self, value):
              self.__lastname = value

     @property
     def location(self):
              return self.__location
     @location.setter
     def location(self, value):
              self.__location = value

     @property
     def password(self):
              return self.__password
     @password.setter
     def password(self, value):
              if len(self.__password) < 8:
                     raise ValueError("the password should be more than (8) Characters")
              self.__password = value

     @property
     def phone_number(self):
              return self.__phone_number
     @phone_number.setter
     def phone_number(self, value):
              if len(self.__phone_number) != 11:
                    raise ValueError("Phone number must have (11) digits")
              self.__phone_number = value

     @property
     def email(self):
              return self.__email
     @email.setter
     def email(self, value):
              self.__email = value

     @property
     def shopping_cart(self):
         return self.__shopping_cart
     @shopping_cart.setter
     def shopping_cart(self, value):
         self.__shopping_cart = value

     @property
     def balance(self):
         return self.__balance
     @balance.setter
     def balance(self, value):
         self.__balance = value



