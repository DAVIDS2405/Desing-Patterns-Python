from abc import ABC, abstractmethod

class SaleComponent(ABC):
    @abstractmethod
    def get_total(self):
        pass
    
    @abstractmethod
    def details (self,space=0):
        pass
    
    
    
class Product (SaleComponent):
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price
        
    def get_total(self):
        return self.__price
    
    def details (self,space=0):
        print(" " * space + f"Product: {self.__name}, Price: {self.get_total()}")
        
        
class Package (SaleComponent):
    def __init__(self, name: str):
        self.__name = name
        self.__products = []
        
    def add(self, product: SaleComponent):
        self.__products.append(product)
        
    def remove(self, product: SaleComponent):
        self.__products.remove(product)
        
    def get_total(self):
        total = 0
        for product in self.__products:
            total += product.get_total()
        return total
    
    def details (self,space=0):
        print(" " * space + f"Package: {self.__name}, Total Price: {self.get_total()}")
        for product in self.__products:
            product.details(space + 2)
            
            
product1 = Product("Product 1", 10.0)
product2 = Product("Product 2", 20.0)
product3 = Product("Product 3", 30.0)
product4 = Product("Product 4", 40.0)

max_package = Package("Max Package")
max_package.add(product1)
max_package.add(product2)


max_package2 = Package("Max Package 2")
max_package2.add(product3)
max_package2.add(product4)

sale_package = Package("Sale Package")
sale_package.add(max_package)
sale_package.add(max_package2)

sale_package.details()