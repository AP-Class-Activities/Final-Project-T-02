import pickle


class Product:

    def __init__(self, store, name, explanation, image='./DATABASE/ProductPic.png'):
        self.__store = store
        self.__name = name
        self.__explanation = explanation
        self.__product_id = self.__gen_product_id()
        self.__sellers_prices_stock = {}
        self.__comments = []
        self.__image = image
        self.__save()

        with open(f"./DATABASE/{self.__store}/Products/ProductsList.txt", "at") as products:
            products.write("\n" + self.__product_id)


    # -------------- Private Methods --------------

    # to save changes to database
    def __save(self):
        with open(f"./DATABASE/{self.__store}/Products/{self.__product_id}.dat", "wb") as dat_file:
            pickle.dump(self, dat_file)


    # to generate unique product id
    def __gen_product_id(self):
        try:
            with open(f"./DATABASE/{self.__store}/Products/ProductsList.txt", "rt") as products:
                for line in products:
                    pass
                last_product_id = int(line[2:])
        except UnboundLocalError:
            last_product_id = 0  # in case there are no products yet
        
        return "PR" + (6 - len(str(last_product_id+1))) * "0" + str(last_product_id+1)


    # -------------- Public Methods --------------

    # to change product's stock or price
    def change_stock_price(self, seller, price, stock):
        if not isinstance(price, int) and isinstance(stock, int):
            raise ValueError("price and stock must be integers")
        
        self.__sellers_prices_stock[seller] = [price, stock]
        self.__save()


    # to decrease stock after a purchase
    def decrease_stock(self, seller, number):
        if number > self.__sellers_prices_stock[seller][1]:
            raise ValueError("there are not enough products in stock")

        self.__sellers_prices_stock[seller][1] -= number
        self.__save()


    # to add new comments
    def add_comment(self, sender, comment):
        if not isinstance(comment, str):
            raise ValueError("comment must be a string")
        
        self.__comments.append([sender, comment])
        self.__save()


    # to get price of a particular seller
    def price(self, seller):
        if not (seller in self.sellers):
            raise ValueError("no such seller")

        return self.__sellers_prices_stock[seller][0]


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
    def explanation(self):
        return self.__explanation

    @explanation.setter
    def explanation(self, value):
        if not isinstance(value, str):
            raise ValueError("explanation must be a string")
        
        self.__explanation = value
        self.__save()


    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        if not isinstance(value, str):
            raise ValueError("image path must be a string")
        if not value.lower().endswith((".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif")):
            raise ValueError("image format not supported")
        self.__image = value
        self.__save()


    @property
    def product_id(self):
        return self.__product_id


    @property
    def least_price(self):
        return min([i[0] for i in self.__sellers_prices_stock.values()])


    @property
    def sum_stocks(self):
        return sum([i[1] for i in self.__sellers_prices_stock.values()])


    @property
    def comments(self):
        return self.__comments

    @property
    def sellers(self):
        sellers_list = []
        for seller in list(self.__sellers_prices_stock.keys()):
            if self.__sellers_prices_stock[seller][1] > 0:
                sellers_list.append(seller)
        return sellers_list
    
