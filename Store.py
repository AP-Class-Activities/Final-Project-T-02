import pickle
import os
import random
import string
import datetime
from Product import Product
from Seller import Seller
from User import User


class Store:
    
    def __init__(self, name, owner_name, owner_password):
        self.__name = name
        self.__owner_name = owner_name
        self.__owner_password = owner_password
        self.__products = []
        self.__sellers = []
        self.__users = []
        self.__pending_sellers = []
        self.__pending_products = []
        self.__promo_codes = {}
        self.__save()

        # creating necessary directories
        os.mkdir(f"./DATABASE/{self.__name}")
        os.mkdir(f"./DATABASE/{self.__name}/Products")
        os.mkdir(f"./DATABASE/{self.__name}/Sellers")
        os.mkdir(f"./DATABASE/{self.__name}/Users")
        os.mkdir(f"./DATABASE/{self.__name}/Purchases")

        with open(f"./DATABASE/StoresList.txt", "at") as stores:
            stores.write("\n" + self.__name)


    # -------------- Private Methods --------------

    # to save changes to database
    def __save(self):
        with open(f"./DATABASE/{self.__name}.dat", "wb") as dat_file:
            pickle.dump(self, dat_file)


    # to load saved data from database
    def __load(self):

        # loading products
        with open(f"./DATABASE/{self.__name}/Products/ProductsList.txt", "rt") as products_list:
            for line in products_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Products/{line[:len(line)-1]}.dat", "rb") as product:
                        self.__products.append(pickle.load(product))

        # loading sellers
        with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt", "rt") as sellers_list:
            for line in sellers_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Sellers/{line[:len(line)-1]}.dat", "rb") as seller:
                        self.__sellers.append(pickle.load(seller))

        # loading users
        with open(f"./DATABASE/{self.__name}/Users/SellersList.txt", "rt") as users_list:
            for line in users_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Users/{line[:len(line)-1]}.dat", "rb") as user:
                        self.__users.append(pickle.load(user))


    # -------------- Public Methods --------------

    # to add new products to pending list
    def add_new_product(self, product):

        # value constraints:
        if not isinstance(product, list):
            raise ValueError("product must be a list with product's name and explanation in it")
        if len(product) != 2:
            raise ValueError("product must only contain name and explanation")
        if not (isinstance(product[0], str) and isinstance(product[1], str)):
            raise ValueError("name and explanation must be strings")

        self.__pending_products.append(product)
        self.__save()


    # to add new sellers to pending list
    def seller_sign_up(self, name, email, password, location):
        self.__load()

        # value constraints:
        for seller in self.__sellers:
            if email == seller.email:
                raise ValueError("email already used")
        if len(password) != 8:
            raise ValueError("password must be 8 characters")
        if not (isinstance(location[0], float) and isinstance(location[1], float)):
            raise ValueError("location must be a tuple of two floating points")

        new_seller = [name, email, password, location]
        self.__pending_sellers.append(new_seller)
        self.__save()


    # for sellers' log-in
    def seller_sign_in(self, email, password):
        self.__load()
        for seller in self.__sellers:
            if seller.email == email and seller.password == password:
                    return True
        return False


    # to remove sellers
    def remove_seller(self, seller_id):

        # value constraint:
        if not isinstance(seller_id, str):
            raise ValueError("seller id must be a string")

        # removing related file and from list
        if os.path.exists(f"./DATABASE/{self.__name}/Sellers/{seller_id}.dat"):
            os.remove(f"./DATABASE/{self.__name}/Sellers/{seller_id}.dat")
            with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt", "rt") as sellers_list_file:
                sellers_list = sellers_list_file.readlines()
            with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt", "wt") as sellers_list_file:
                for line in sellers_list:
                    if line.strip("\n") != seller_id:
                        sellers_list_file.write(line)


    # to make new users
    def user_sign_up(self, name, email, password, location):

        # value constraints:
        self.__load()
        for user in self.__users:
            if user.email == email:
                raise ValueError("email already used")
        if len(password) != 8:
            raise ValueError("password must be 8 characters")
        if not (isinstance(location[0], float) and isinstance(location[1], float)):
            raise ValueError("location must be a tuple of two floating points")

        User(self, name, email, password, location)


    # for users' log-in
    def user_sign_in(self, email, password):
        self.__load()
        for user in self.__users:
            if user.email == email and user.password == password:
                return True
        return False


    # to remove users
    def remove_user(self, user_id):

        # value constraint:
        if not isinstance(user_id, str):
            raise ValueError("user id must be a string")

        # removing related file and from list
        if os.path.exists(f"./DATABASE/{self.__name}/Users/{user_id}.dat"):
            os.remove(f"./DATABASE/{self.__name}/Users/{user_id}.dat")
            with open(f"./DATABASE/{self.__name}/Users/UsersList.txt", "rt") as users_list_file:
                users_list = users_list_file.readlines()
            with open(f"./DATABASE/{self.__name}/Users/UsersList.txt", "wt") as users_list_file:
                for line in users_list:
                    if line.strip("\n") != user_id:
                        users_list_file.write(line)


    # for store owner to allow new sellers
    def confirm_new_seller(self, seller_number):
        
        # value constraint:
        if not isinstance(seller_number, int):
            raise ValueError("seller number must be an integer")

        Seller(*self.__pending_sellers[seller_number])


    # for sellers to add products to pending list
    def add_pending_product(self, name, explanation):
        self.__pending_products.append((self, name, explanation))
        self.__save()

    
    # for store owner to allow new products
    def confirm_new_product(self, product_number):

        # value constraint:
        if not isinstance(product_number, int):
            raise ValueError("product number must be an integer")
        
        Product(*self.__pending_products[product_number])


    # to generate a promo code
    def gen_promo_code(self, percentage, expiration=30, products=None, users=None):

        # value constraints:
        if not isinstance(percentage, int):
            raise ValueError("percentage must be an integer")
        if not isinstance(expiration, int):
            raise ValueError("expiration must be an integer indicating the number of days")
        if products:  # if it's not None
            if not isinstance(products, list):
                raise ValueError("products must be a list of products")
            for product in products:
                if not isinstance(product, Product):
                    raise ValueError("products must only contain objects of type Product")
        else:
            self.__load()
            products = self.__products  # if no products are specified, all products will be used
        if users:  # if it's not None
            if not isinstance(users, list):
                raise ValueError("users must be a list of users")
            for user in users:
                if not isinstance(user, User):
                    raise ValueError("users must only contain objects of type User")
        else:
            self.__load()
            users = self.__users  # if no users are specified, all users will be used

        promo_code = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.__promo_codes[promo_code] = (percentage, expiration, products, users)
        self.__save()
        return promo_code


    # to get profits within desired period
    def profit(self, start_date, end_date):
        sum_profits = 0
        start_date = datetime.datetime(*[int(_) for _ in start_date.split("-")])
        end_date = datetime.datetime(*[int(_) for _ in end_date.split("-")])
        for file in os.listdir(f"./DATABASE/{self.__name}/Purchases"):
            file_date = datetime.datetime(*[int(_) for _ in file[:10].split("-")])
            if start_date < file_date < end_date:
                with open(f"./DATABASE/{self.__name}/Purchases/{file}", "rt") as file_info:
                    sum_profits += 0.2 * list(file_info)[1]


    # -------------- Setters and Getters --------------

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        
        self.__name = value
        self.__save()


    @property
    def owner_name(self):
        return self.__owner_name
    
    @owner_name.setter
    def owner_name(self, value):
        if not isinstance(value, str):
            raise ValueError("owner name must be a string")
        
        self.__owner_name = value
        self.__save()


    @property
    def owner_password(self):
        return self.__owner_password
    
    @owner_password.setter
    def owner_password(self, value):
        if len(value) != 8:
            raise ValueError("password must be 8 characters")
        
        self.__owner_password = value
        self.__save()


    @property
    def products(self):
        self.__load()
        return self.__products


    @property
    def sellers(self):
        self.__load()
        return self.__sellers


    @property
    def users(self):
        self.__load()
        return self.__users


    @property
    def pending_sellers(self):
        return self.__pending_sellers


    @property
    def pending_products(self):
        return self.__pending_products


    @property
    def promo_codes(self):
        return list(self.__promo_codes.keys())
