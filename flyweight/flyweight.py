from abc import ABC, abstractmethod

class Flyweight(ABC):
    @abstractmethod
    def print(self, size:int):
        pass
    
    
class ConcreteFlyweight(Flyweight):
    def __init__(self, character: str):
        self.__character = character #compartido 
    
    def print(self, size:int): # no compartido 
        print(f"Name: {self.__character}, Size: {size}")
        
        
class FlyweightFactory:
    def __init__(self):
        self.__flyweights = {}
        
    def get(self, character: str) -> Flyweight:
        if character not in self.__flyweights:
            print(f"Creating flyweight for {character}")
            self.__flyweights[character] = ConcreteFlyweight(character)
            
        return self.__flyweights[character]
    
    
flyweight_factory = FlyweightFactory()

a1 = flyweight_factory.get("a")
a1.print(10)
a2 = flyweight_factory.get("a")
a2.print(20)
a3 = flyweight_factory.get("a")
a3.print(30)


