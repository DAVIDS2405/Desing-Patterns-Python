from abc import ABC, abstractmethod

class TaxStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass 

class IVAStrategy(TaxStrategy):  
    def calculate(self, amount: float) -> float:
        return amount * 0.16
    
class ISRStrategy(TaxStrategy):  
    def calculate(self, amount: float) -> float:
        return amount * 0.30

class IEPSStrategy(TaxStrategy):  
    def calculate(self, amount: float) -> float:
        return amount * 0.53
    
class TaxCalculator:
    def __init__(self, strategy: TaxStrategy):
        self.__strategy = strategy

    def set_strategy(self, strategy: TaxStrategy):
        self.__strategy = strategy

    def calculate(self, amounts: list[float]) -> list[float]:
        taxes = []
        for amount in amounts:
            taxes.append(self.__strategy.calculate(amount))
        return taxes 

amounts = [100,30,18]
iva_strategy = IVAStrategy()
isr_strategy = ISRStrategy()
ieps_strategy = IEPSStrategy()
tax_calculator = TaxCalculator(iva_strategy)

print(tax_calculator.calculate(amounts))

tax_calculator.set_strategy(isr_strategy)
print(tax_calculator.calculate(amounts))

tax_calculator.set_strategy(ieps_strategy)
print(tax_calculator.calculate(amounts))