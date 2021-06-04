'''

Author: Anita Karimi
Email: anita.karimi.17@gmail.com

Usage:
   1) Create a new user:
        u = user(name, lastname, location, username, password, purchase_history, wallet, phone_number, orders, email)

   2) Print the user information:
        print(u)
'''

class user:
     def __init__(self, name, lastname, location, username, password, purchase_history, wallet, phone_number, orders, email):
          self.__name = name
          self.__lastname = lastname
          self.__location = location
          self.__username = username
          self.__password = password
          self.__purchase_history =  purchase_history
          self.__wallet = wallet
          self.__phone_number = phone_number
          self.__orders = orders
          self.__email = email


    ##setters and getters

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
     def username(self):
              return self.__username

     @username.setter
     def username(self, value):
              self.__username = value

     @property
     def password(self):
              return self.__password

     @password.setter
     def password(self, value):
              self.__password = value

     @property
     def purchase_history(self):
              return self.__purchase_history

     @purchase_history.setter
     def purchase_history(self, value):
              self.__purchase_history = value

     @property
     def wallet(self):
              return self.__wallet

     @wallet.setter
     def wallet(self, value):
              self.__wallet = value

     @property
     def phone_number(self):
              return self.__phone_number

     @phone_number.setter
     def phone_number(self, value):
              self.__phone_number = value

     @property
     def orders(self):
              return self.__orders

     @orders.setter
     def orders(self, value):
              self.__orders = value

     @property
     def email(self):
              return self.__email

     @email.setter
     def email(self, value):
              self.__email = value














