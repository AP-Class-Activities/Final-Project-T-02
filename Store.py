from Product import Product
import pickle
import os
from Seller import Seller
from User import User


class Store:
    
    def __init__(self, name, owner_name, owner_password):
        self.__name = name
        self.__owner_name = owner_name
        self.__owner_password = owner_password
        self.__products = []
        self.__sellers = {}
        self.__users = {}
        self.__pending_sellers = []
        self.__pending_products = []
        self.__save()

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


    def __load(self):
        with open(f"./DATABASE/{self.__name}/Products/ProductsList.txt") as products_list:
            for line in products_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Products/{line[:len(line)-1]}.dat") as product:
                        self.__products.append(pickle.load(product))

        with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt") as sellers_list:
            for line in sellers_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Sellers/{line[:len(line)-1]}.dat") as seller:
                        self.__sellers.append(pickle.load(seller))

        with open(f"./DATABASE/{self.__name}/Users/SellersList.txt") as users_list:
            for line in users_list:
                if line != "\n":
                    with open(f"./DATABASE/{self.__name}/Users/{line[:len(line)-1]}.dat") as user:
                        self.__users.append(pickle.load(user))


    # -------------- Public Methods --------------

    def seller_sign_up(self, name, email, password, location):
        for seller in self.__sellers:
            if email == seller.email:
                raise ValueError("email already used")
        if len(password) != 8:
            raise ValueError("password must be 8 characters")
        if not (isinstance(location[0], float) and isinstance(location[1], float)):
            raise ValueError("location must be a tuple of two floating points")

        new_seller = [name, email, password, location]
        self.__pending_sellers.append(new_seller)
    
    def seller_sign_in(self, email, password):
        for seller in self.__sellers:
            if seller.email == email and seller.password == password:
                    return True
        return False


    def user_sign_up(self, name, email, password, location):
        for user in self.__users:
            if user.email == email:
                raise ValueError("email already used")
        if len(password) != 8:
            raise ValueError("password must be 8 characters")
        if not (isinstance(location[0], float) and isinstance(location[1], float)):
            raise ValueError("location must be a tuple of two floating points")

        User(self, name, email, password, location)


    def user_sign_in(self, email, password):
        for user in self.__users:
            if user.email == email and user.password == password:
                return True
        return False


    def confirm_new_seller(self, seller_number):
        if not isinstance(seller_number, int):
            raise ValueError("seller number must be an integer")

        Seller(*self.__pending_sellers[seller_number])


    def confirm_new_product(self, product_number):
        if not isinstance(product_number, int):
            raise ValueError("product number must be an integer")
        
        Product(*self.__pending_products[product_number])


    # add product soon


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

