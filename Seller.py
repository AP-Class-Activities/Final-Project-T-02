class Seller:
    def __init__(self,store,name,family,address,phone,email):
        self.__store = store
        self.__name = name
        self.__family=family
        self.__address = address
        self.__phone = phone
        self.__email = email

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
