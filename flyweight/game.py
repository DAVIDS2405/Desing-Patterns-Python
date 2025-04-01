from abc import ABC, abstractmethod


class TypeCar(ABC):
    @abstractmethod
    def print(self, x:int, y:int):
        pass
    
    
class TypeCarCommon(TypeCar):
    def __init__(self, name: str,color: str,model: str):
        self.__color = color
        self.__model = model
        self.__name = name # compartido
    
    def print(self, x:int, y:int): # no compartido 
        print(f"Name: {self.__name}, X: {x}, Y: {y}")
        
        
        
class TypeCarFactory:
    def __init__(self):
        self.__type_cars = {}
        
    def get(self, name: str,color: str,model: str) -> TypeCar:
        key =(name,color,model) 
        if key not in self.__type_cars:
            print(f"Creating type car for {name} {color} {model}")
            self.__type_cars[key] = TypeCarCommon(name,color,model)
            
        return self.__type_cars[key]
    

class Car:
    def __init__(self,x,y,type_car: TypeCar):
        self.x = x
        self.y= y
        self.__type_car = type_car
        
    def print(self ):
        self.__type_car.print(self.x,self.y)
        
        
class Game:
    def __init__(self):
        self.__type_car_factory = TypeCarFactory()
        self.__cars = []
        
    def add(self,x:int,y:int,name: str,color: str,model: str):
        type_car = self.__type_car_factory.get(name,color,model)
        car = Car(x,y,type_car)
        self.__cars.append(car)
        
    def print(self):
        for car in self.__cars:
            car.print()
            
            
game = Game()
game.add(10,20,"Car1","Red","Model1")
game.add(20,20,"Car1","Red","Model1")
game.add(30,40,"Car2","Blue","Model1")
game.add(111,40,"Car2","Blue","Model1")

game.print()