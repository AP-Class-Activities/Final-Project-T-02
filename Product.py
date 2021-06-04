import json


class Product:

    def __init__(self, store, name, explanation):
        self.__store = store
        self.__load()
        self.__name = name
        self.__explanation = explanation
        self.__product_id = self.__gen_product_id()
        self.__sellers_prices_stock = {}
        self.__comments = []
        self.__save()


    # -------------- Private Methods --------------

    # to load products information from database
    def __load(self):
        with open(f"./DATABASE/{self.__store}/products.json", "rt") as products_json:
            self.__products_json = json.load(products_json)
        self.__name, self.__explanation, self.__sellers_prices_stock, self.__comments = self.__products_json[self.__product_id]


    # to save changes to database
    def __save(self):
        self.__products_json[self.__product_id] = [self.__name, self.__explanation, self.__sellers_prices_stock, self.__comments]

        with open(f"./DATABASE/{self.__store}/products.json", "wt") as products_json:
            json.dump(self.__products_json, products_json)


    # to generate unique product id
    def __gen_product_id(self):
        try:
            last_product_id = int(list(self.__products_json.keys())[-1][2:])
        except IndexError:
            last_product_id = 0  # in case there are no products yet
        
        return "PR" + (6 - len(str(last_product_id+1))) * "0" + str(last_product_id+1)


    # -------------- Public Methods --------------
    
    # to increase/add-to product's stock
    def add_stock(self, seller, price, stock):
        self.__load()
        self.__sellers_prices_stock[seller] = (price, stock)
        self.__save()


    # to add new comments
    def add_comment(self, sender, comment):
        self.__load()
        self.__comments.append([sender, comment])
        self.__save()


    # -------------- Setters and Getters --------------

    @property
    def name(self):
        self.__load()
        return self.__name

    @name.setter
    def name(self, value):
        self.__load()
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self.__name = value
        self.__save()


    @property
    def explanation(self):
        self.__load()
        return self.__explanation

    @explanation.setter
    def explanation(self, value):
        self.__load()
        if not isinstance(value, str):
            raise ValueError("explanation must be a string")
        self.__explanation = value
        self.__save()


    @property
    def price(self):
        self.__load()
        return min([i[0] for i in self.__sellers_prices_stock.values()])


    @property
    def stock(self):
        self.__load()
        return sum([i[1] for i in self.__sellers_prices_stock.values()])


    @property
    def comments(self):
        self.__load()
        return self.__comments

