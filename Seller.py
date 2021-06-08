import pickle 
import datetime
import os

class Seller:
    def _init_(self,store,name,family,password,address,phone,email):
        self.__store = store
        self.__name = name
        self.__family = family
        self.__password = password
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__seller_id = self._gen_seller_id()
        self.__products = {}
        self.__rating = []
        self.__save()

        with open(f"./DATABASE/{self.__store}/Sellers/SellersList.txt", "at") as sellers:
            sellers.write("\n" + self.__seller_id)




    def __gen_seller_id(self):
        try:
            with open(f"./DATABASE/{self.__store}/Sellers/SellersList.txt", "rt") as seller:
                for line in seller:
                    pass
                last_seller_id = int(line[2:].strip("\n"))
        except FileNotFoundError:
            last_seller_id = 0  # in case there are no sellers yet
        
        return "SE" + (6 - len(str(last_seller_id+1))) * "0" + str(last_seller_id+1)


    def __save(self):
        with open(f"./DATABASE/{self._store}/Sellers/{self._seller_id}.dat","wb") as dat_file: 
            pickle.dump(self, dat_file)


    def create_new_product(self,name,explanation):
        with open(f"./DATABASE/{self.__store}.dat","rb") as store_file:
            store = pickle.load(store_file)
            store.add_new_product(name,explanation)


    def add_product_stock(self,product,price,stock):
        with open(f"./DATABASE/{self.__store}/Products/{product}","rb") as product_file:
            product = pickle.load(product_file)


        product.change_stock_price(self.__seller_id,price,stock)
        self.__products[product] =[price,stock]
        self.__save()


    def profit(self, start_date, end_date):
        sum_profits = 0
        start_date = datetime.datetime(*[int(_) for _ in start_date.split("-")])
        end_date = datetime.datetime(*[int(_) for _ in end_date.split("-")])
        for file in os.listdir(f"./DATABASE/{self.__name}/Purchases"):
            file_date = datetime.datetime(*[int(_) for _ in file[:10].split("-")])
            if start_date < file_date < end_date:
                with open(f"./DATABASE/{self.__name}/Purchases/{file}", "rt") as file_info:
                    sum_profits += 0.2 * list(file_info)[1]
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
