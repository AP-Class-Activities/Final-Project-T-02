'''

Email: anita.karimi.17@gmail.com

'''

import pickle
import os
import random
from Product import Product
from Seller import Seller


class User:
     def __init__(self,store, name, lastname, location, password, phone_number, email, shopping_cart, balance):
         self.__store = store
         self.__name = name
         self.__lastname = lastname
         self.__location = location
         self.__password = password
         self.__phone_number = phone_number
         self.__email = email
         self.__shopping_cart = shopping_cart
         self.__balance = balance
         self.__save()



     #directories

     os.mkdir(f"./DATABASE/{self.__name }/User")


   #Methods

     #create a new user

     def create_new_user(self, name, lastname, password, phone_number, location):

         self.__load()
         for user in self.__user:
             if user.phone_number == phone_number:
                 raise ValueError("This phone number already used")
         if len(password) != 8:
             raise ValueError("the password should be more than (8) Characters")

         user(self, name, lastname, password, phone_number, location)


     #user sign-in

     def user_sign_in(self, username, password):
        self.__load()
        for user in self.__user:
            if user.username == username and user.password == password:
                return True
            else:
                return False

     #Increase the wallet balance

     def Increase_wallet_balance(self, balance):
         addition = 0
         for user in self.__user:
             user.__balance += addition
             break

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



