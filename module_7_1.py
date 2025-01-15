class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'w')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        read = file.read()
        file.close()
        return read

    def add(self, *products):
        for product in products:
            if product.name and product.category not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                # не смог решить условие с увеличением веса
                print(f'Продукт {product.name} уже есть в магазине, его общий вес теперь равен ?')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())



