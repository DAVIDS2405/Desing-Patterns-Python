from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass

class LocalTaxCalculator(TaxCalculator):
    def calculate(self, amount):
        return amount * 0.16
    
class ForeignTaxCalculator(TaxCalculator):
    def calculate(self, amount):
        return amount * 0.50
    
class ZeroTaxCalculator(TaxCalculator):
    def calculate(self, amount):
        return 0
    
class AbstractSale(ABC):
    def __init__(self, tax_calculator: TaxCalculator, concepts):
        self.tax_calculator = tax_calculator
        self.concepts = concepts 

    @abstractmethod
    def calculate_total(self):
        pass

class Sale(AbstractSale):
    def calculate_total(self):
        total = sum(self.concepts)
        return total + self.tax_calculator.calculate(total)
    
    
sale = Sale(LocalTaxCalculator(), [100, 200, 300])
print(sale.calculate_total())

sale2 = Sale(ForeignTaxCalculator(), [100, 200, 300])
print(sale2.calculate_total())

sale3 = Sale(ZeroTaxCalculator(), [100, 200, 300])
print(sale3.calculate_total())