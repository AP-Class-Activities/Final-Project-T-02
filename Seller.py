import pickle

class Seller:
    def __init__(self,store,name,family,address,phone,email):
        self.__store = store
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__selller_id = self.__gen_seller_id()
        self.__save()


    def __gen_seller_id(self):
        try:
            with open(f"./DATABASE/{self.__store}/Seller/SellerList.txt", "rt") as seller:
                for line in seller:
                    pass
                last_seller_id = int(line[2:].strip("\n"))
        except FileNotFoundError:
            last_seller_id = 0  # in case there are no sellers yet
        
        return "SE" + (6 - len(str(last_seller_id+1))) * "0" + str(last_seller_id+1)


    def __save(self):
        with open(f"./DATABASE/{self.__store}/Seller/{self.__seller_id}.dat","wb") as dat_file: 
            pickle.dump(self, dat_file)


    def create_new_seller(self,name,explanation):
        with open(f"./DATABASE/{self.__store}.dat","rb") as store_file:
            store = pickle.load(store_file)
            store.add_pending_seller(name,explanation)   


    # setters and getters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property 
    def family(self):
        return self.__family

    @family.setter
    def family(self,value):
        self.__family = value

    @property 
    def address(self):
        return self.__address

    @address.setter
    def address(self,value):
        self.__address = value
    
    @property 
    def email(self):
        return self.__email

    @email.setter
    def email(self,value):
        self.__email = value   
    
    @property 
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self,value):
        self.__phone = value
