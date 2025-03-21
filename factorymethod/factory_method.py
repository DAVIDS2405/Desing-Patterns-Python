from abc import ABC, abstractmethod

class Concept(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def price(self) -> float:
        pass

class Product(Concept):
    def __init__(self, amount, tax):
        self.__amount = amount
        self.__tax = tax

    def description(self) -> str:
        return "Producto"
    
    def price(self) -> float:
        return self.__amount + self.__tax
    
class Service(Concept):
    def __init__(self, amount):
        self.__amount = amount

    def description(self) -> str:
        return "Servicio"
    
    def price(self) -> float:
        return self.__amount

class ConceptFactory(ABC): 
    def __init__(self, *args):
        self._args = args
     
    @abstractmethod
    def create(self) -> Concept:
        pass 

class ProductFactory(ConceptFactory):
    def create(self) -> Concept:
        return Product(self._args[0], self._args[1])
    
class ServiceFactory(ConceptFactory):
    def create(self) -> Concept:
        return Service(self._args[0])


def show_info(concept: Concept):
    print(f"El concepto es un {concept.description()}")

product_factory = ProductFactory(10, 2)
service_factory = ServiceFactory(20)

concept1 = product_factory.create()
concept2 = service_factory.create()
concept3 = product_factory.create()

show_info(concept1)
show_info(concept2)

print(concept1.price())
print(concept2.price())
print(concept3.price())
