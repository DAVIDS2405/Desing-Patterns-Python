from abc import ABC, abstractmethod

class Implementor(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass 

class AddCalculation(Implementor):
    def calculate(self, a: float, b: float) -> float:
        return a + b
    
class MulCalculation(Implementor):
    def calculate(self, a: float, b: float) -> float:
        return a * b

class Abstraction(ABC):
    def __init__(self, calculation: Implementor, numbers):
        self.calculation = calculation
        self.numbers = numbers

    @abstractmethod
    def print(self, n: float):
        pass 

class Numbers(Abstraction):

    def print(self, n: float):
        for number in self.numbers:
            print(self.calculation.calculate(number, n))

add = AddCalculation()
mul = MulCalculation()

numbers = Numbers(add, [1,2,3,4])
numbers.print(2)

print("-------------")

numbers2 = Numbers(mul, [1,2,3,4])
numbers2.print(2)