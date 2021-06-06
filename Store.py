import pickle
import os
import random
import string
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
        with open(f"./DATABASE/{self.__name}/Products/ProductsList.txt") as products_list:
            for line in products_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Products/{line[:len(line)-1]}.dat") as product:
                        self.__products.append(pickle.load(product))

        # loading sellers
        with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt") as sellers_list:
            for line in sellers_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Sellers/{line[:len(line)-1]}.dat") as seller:
                        self.__sellers.append(pickle.load(seller))

        # loading users
        with open(f"./DATABASE/{self.__name}/Users/SellersList.txt") as users_list:
            for line in users_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Users/{line[:len(line)-1]}.dat") as user:
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


    # for store owner to allow new sellers
    def confirm_new_seller(self, seller_number):
        
        # value constraint:
        if not isinstance(seller_number, int):
            raise ValueError("seller number must be an integer")

        Seller(*self.__pending_sellers[seller_number])


    # for store owner to allow new products
    def confirm_new_product(self, product_number):

        # value constraint:
        if not isinstance(product_number, int):
            raise ValueError("product number must be an integer")
        
        Product(*self.__pending_products[product_number])


    # to generate a promo code
    def gen_promo_code(self, expiration=30, products=None):

        # value constraints:
        if not isinstance(expiration, int):
            raise ValueError("expiration must be an integer indicating the number of days")
        if Product:  # if it's not None
            if not isinstance(products, list):
                raise ValueError("products must be a list of products")
            for product in products:
                if not isinstance(product, Product):
                    raise ValueError("products must only contain objects of type Product")
        else:
            self.__load()
            products = self.__products  # if no products are specified, all products will be used

        promo_code = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        self.__promo_codes[promo_code] = (expiration, products)
        self.__save()
        return promo_code


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

