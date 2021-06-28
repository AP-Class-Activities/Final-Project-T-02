import pickle 
import datetime
import os

class Seller:
    def __init__(self,store,name,family,password,address,phone,email):
        self.__store = store
        self.__name = name
        self.__family = family
        self.__password = password
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__seller_id = self.__gen_seller_id()
        self.__products = {}
        self.__rating = []
        self.__save()

        with open(f"./DATABASE/{self.__store.name}/Sellers/SellersList.txt", "at") as sellers:
            sellers.write("\n" + self.__seller_id)




    def __gen_seller_id(self):
        try:
            with open(f"./DATABASE/{self.__store.name}/Sellers/SellersList.txt", "rt") as seller:
                for line in seller:
                    pass
                last_seller_id = int(line[2:].strip("\n"))
        except UnboundLocalError:
            last_seller_id = 0  # in case there are no sellers yet

        return "SE" + (6 - len(str(last_seller_id+1))) * "0" + str(last_seller_id+1)


    def __save(self):
        with open(f"./DATABASE/{self.__store.name}/Sellers/{self.__seller_id}.dat","wb") as dat_file: 
            pickle.dump(self, dat_file)


    def create_new_product(self,name,explanation, image='./DATABASE/Icons/ProductPic.png'):
        with open(f"./DATABASE/{self.__store.name}.dat","rb") as store_file:
            store = pickle.load(store_file)
            store.add_new_product(name,explanation, image)


    def add_product_stock(self,product,price,stock):
        product.change_stock_price(self, price,stock)
        self.__products[product] =[price,stock]
        self.__save()


    def profit(self, start_date, end_date):
        sum_profits = 0
        start_date = datetime.datetime(*[int(_) for _ in start_date.split("-")])
        end_date = datetime.datetime(*[int(_) for _ in end_date.split("-")])
        for purchase in self.sells:
            file_date = datetime.datetime(*purchase[0].split("-"))
            if start_date < file_date < end_date:
                sum_profits += 0.8 * purchase[-1] * purchase[-2]
        return sum_profits



    # setters and getters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
        self.__save()

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self,value):
        self.__family = value
        self.__save()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self,value):
        self.__address = value
        self.__save()
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,value):
        self.__email = value   
        self.__save()
    
    @property 
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self,value):
        self.__phone = value
        self.__save()


    @property 
    def password(self):
        return self.__password

    @password.setter
    def password(self,value):
        self.__password = value
        self.__save()

    @property
    def sells(self):
        return self.__store.get_sells(self.__seller_id)

    @property
    def rating(self):
        return self.__rating[1]/self.__rating[0]

    @rating.setter
    def rating(self, value):
        self.__rating[0] += 1
        self.__rating[1] += value
        self.__save()

    @property
    def seller_id(self):
        return self.__seller_id
