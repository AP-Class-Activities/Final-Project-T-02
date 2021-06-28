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
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(owner_name, str):
            raise ValueError("owner name must be a string")
        if not (isinstance(owner_password, str) and len(owner_password) == 8):
            raise ValueError("owner password must be a string of 8 characters")
                     
        self.__name = name
        self.__owner_name = owner_name
        self.__owner_password = owner_password
        self.__products = []
        self.__sellers = []
        self.__users = []
        self.__pending_sellers = []
        self.__pending_products = []
        self.__promo_codes = {}
        self.__purchases = []
        self.__save()

        # creating necessary directories
        os.mkdir(f"./DATABASE/{self.__name}")
        os.mkdir(f"./DATABASE/{self.__name}/Products")
        os.mkdir(f"./DATABASE/{self.__name}/Sellers")
        os.mkdir(f"./DATABASE/{self.__name}/Users")
        os.mkdir(f"./DATABASE/{self.__name}/Purchases")

        with open(f"./DATABASE/{self.__name}/Products/ProductsList.txt", "wt") as _:
            pass
        with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt", "wt") as _:
            pass
        with open(f"./DATABASE/{self.__name}/Users/UsersList.txt", "wt") as _:
            pass

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
            self.__products = []
            for line in products_list:
                if line != "\n":
                    line = line.strip('\n')
                    with open(f"./DATABASE/{self.__name}/Products/{line}.dat", "rb") as product:
                        self.__products.append(pickle.load(product))

        # loading sellers
        with open(f"./DATABASE/{self.__name}/Sellers/SellersList.txt", "rt") as sellers_list:
            self.__sellers = []
            for line in sellers_list:
                if line != "\n":
                    line = line.strip('\n')
                    with open(f"./DATABASE/{self.__name}/Sellers/{line}.dat", "rb") as seller:
                        self.__sellers.append(pickle.load(seller))

        # loading users
        with open(f"./DATABASE/{self.__name}/Users/UsersList.txt", "rt") as users_list:
            self.__users = []
            for line in users_list:
                if line != "\n":
                    line = line.strip('\n')
                    with open(f"./DATABASE/{self.__name}/Users/{line}.dat", "rb") as user:
                        self.__users.append(pickle.load(user))


    # to load saved data from database
    def __load_locals(self):
        with open(f"./DATABASE/{self.__name}.dat", "rb") as self_file:
            saved = pickle.load(self_file)
            self.__name, self.__owner_name, self.__owner_password, self.__pending_sellers, self.__pending_products,\
            self.__promo_codes, self.__purchases = saved._Store__name, saved._Store__owner_name, saved._Store__owner_password,\
            saved._Store__pending_sellers, saved._Store__pending_products, saved._Store__promo_codes, saved._Store__purchases


    # -------------- Public Methods --------------

    # to add new products to pending list
    def add_new_product(self, name, explanation, image):

        # value constraints:
        if not (isinstance(name, str) and isinstance(explanation, str) and isinstance(image, str)):
            raise ValueError("name, explanation and image path must be strings")
        if not image.lower().endswith((".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif")):
            raise ValueError("image format not supported")

        self.__load_locals()
        self.__pending_products.append([self.__name, name, explanation, image])
        self.__save()


    # to add a new purchase
    def add_purchase(self, purchase):
        self.__purchases.append(purchase)
        self.__save()


    # to add new sellers to pending list
    def seller_sign_up(self, first_name, last_name, password, location, phone, email):
        self.__load()

        # value constraints:
        for _ in (first_name, last_name, password, phone, email):
            if not isinstance(_, str):
                raise ValueError("first name, last name, password, phone and email must be strings")
        for seller in self.__sellers:
            if email == seller.email:
                raise ValueError("email already used")
            if phone == seller.phone:
                raise ValueError("phone number already used")
        if len(password) != 8:
            raise ValueError("password must be 8 characters")
        if not (isinstance(location, tuple) and len(location) == 2):
            raise ValueError("location must be a tuple of two floating points")
        if not (isinstance(location[0], float) and isinstance(location[1], float)):
            raise ValueError("location must be a tuple of two floating points")
        if len(phone) != 11:
            raise ValueError("phone number must have 11 characters")

        new_seller = [self, first_name, last_name, password, location, phone, email]
        self.__load_locals()
        self.__pending_sellers.append(new_seller)
        self.__save()


    # for sellers' log-in
    def seller_sign_in(self, phone, password):
        self.__load()
        for seller in self.__sellers:
            if seller.phone == phone and seller.password == password:
                    return seller
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
    def user_sign_up(self, first_name, last_name, location, password, phone, email):
        self.__load()

        # value constraints:
        for _ in (first_name, last_name, password, phone, email):
            if not isinstance(_, str):
                raise ValueError("first name, last name, password, phone and email must be strings")
        for user in self.__users:
            if email == user.email:
                raise ValueError("email already used")
            if phone == user.phone:
                raise ValueError("phone number already used")
        if len(password) != 8:
            raise ValueError("password must be 8 characters")
        if not (isinstance(location, tuple) and len(location) == 2):
            raise ValueError("location must be a tuple of two floating points")
        if not (isinstance(location[0], float) and isinstance(location[1], float)):
            raise ValueError("location must be a tuple of two floating points")
        if len(phone) != 11:
            raise ValueError("phone number must have 11 characters")

        User(self, first_name, last_name, location, password, phone, email)


    # for users' log-in
    def user_sign_in(self, phone_number, password):
        self.__load()
        for user in self.__users:
            if user.phone_number == phone_number and user.password == password:
                return user
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
        del self.__pending_sellers[seller_number]

    
    # for store owner to allow new products
    def confirm_new_product(self, product_number):

        # value constraint:
        if not isinstance(product_number, int):
            raise ValueError("product number must be an integer")
        
        Product(*self.__pending_products[product_number])
        del self.__pending_products[product_number]


    # for sellers to get their sells
    def get_sells(self, seller_id):
        self.__load_locals()
        sells = []
        for purchase in self.__purchases:
            if purchase[-1] == seller_id:
                sells.append(purchase)
        return sells


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
        self.__load_locals()
        self.__promo_codes[promo_code] = (percentage, expiration, products, users)
        self.__save()
        return promo_code


    # to get profits within desired period
    def profit(self, start_date, end_date):
        sum_profits = 0
        start_date = datetime.datetime(*[int(_) for _ in start_date.split("-")])
        end_date = datetime.datetime(*[int(_) for _ in end_date.split("-")])
        for purchase in self.__purchases:
            file_date = datetime.datetime(*purchase[0].split("-"))
            if start_date < file_date < end_date:
                sum_profits += 0.2 * purchase[-3] * purchase[-2]
        return sum_profits


    # -------------- Setters and Getters --------------

    @property
    def name(self):
        self.__load_locals()
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        
        self.__name = value
        self.__save()


    @property
    def owner_name(self):
        self.__load_locals()
        return self.__owner_name
    
    @owner_name.setter
    def owner_name(self, value):
        if not isinstance(value, str):
            raise ValueError("owner name must be a string")
        
        self.__owner_name = value
        self.__save()


    @property
    def owner_password(self):
        self.__load_locals()
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
        return self.__sellers.sort(key=lambda _ : _.rating, reverse=True)


    @property
    def users(self):
        self.__load()
        return self.__users


    @property
    def pending_sellers(self):
        self.__load_locals()
        return self.__pending_sellers


    @property
    def pending_products(self):
        self.__load_locals()
        return self.__pending_products


    @property
    def promo_codes(self):
        self.__load_locals()
        return list(self.__promo_codes.keys())


    @property
    def purchases(self):
        self.__load_locals()
        return self.__purchases

