import json


class Product:
    
    def __init__(self, store, name, explanation):
        self.__store = store
        self.__load()
        self.__name = name
        self.__explanation = explanation
        self.__product_number = self.__gen_product_number()
        self.__save()
    
    def __load(self):
        with open(f"./DATABASE/{self.__store}/products.json", "rt") as products_json:
            self.__products_json = json.load(products_json)
    
    def __save(self):
        self.__products_json[self.__product_number] = [self.__name, self.__explanation]

        with open(f"./DATABASE/{self.__store}/products.json", "wt") as products_json:
            json.dump(self.__products_json, products_json)

    def __gen_product_number(self):
        try:
            last_product_number = int(list(self.__products_json.keys())[-1][2:])
        except IndexError:
            last_product_number = 0
        
        return "PR" + (6 - len(str(last_product_number+1))) * "0" + str(last_product_number+1)

