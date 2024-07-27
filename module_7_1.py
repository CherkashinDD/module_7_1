class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file_r = open(self.__file_name, 'r')
        file_contents = file_r.read()
        file_r.close()
        return file_contents

    def add(self, *products):
        list_products = self.get_products()
        new_list_products = ''
        for product in products:
            if product.name in list_products + new_list_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                new_list_products += str(product) + '\n'
        if new_list_products:
            file_a = open(self.__file_name, 'a')
            file_a.write(new_list_products)
            file_a.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
