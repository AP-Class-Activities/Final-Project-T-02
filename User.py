'''

Author: Anita Karimi
Email: anita.karimi.17@gmail.com

'''
import pickle
import os
import random

class user:
     def __init__(self, name, lastname, location, username, password, phone_number, email):
          self.__lastname = lastname
          self.__location = location
          self.__username = username
          self.__password = password
          self.__phone_number = phone_number
          self.__email = email
          self.__save()

     #directories
     os.mkdir(f"./DATABASE/{ self.__name }/Users")

   #Methods

     #create a new user

     def create_new_user(self, name, lastname, password, phone_number, location, email):

         self.__load()
         for user in self.__users:
             if user.phone_number == phone_number:
                 raise ValueError("This phone number already used")
         if len(password) != 8:
             raise ValueError("the password should be more than (8) Characters")
         user(self, name, lastname, password, phone_number, location, email)


     #user sign-in

     def user_sign_in(self, username, password):
        self.__load()
        for user in self.__users:
            if user.username == username and user.password == password:
                return True
            else:
                return False


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











