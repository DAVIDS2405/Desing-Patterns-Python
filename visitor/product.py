from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Book(Product):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        visitor.visit_book(self)


class Food(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        visitor.visit_food(self)


class CalculatorVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_food(self, food):
        pass


class TaxCalculator(CalculatorVisitor):
    def visit_book(self, book):
        print(f"Calculating tax for book '{book.title}' by {book.price}")

    def visit_food(self, food):
        print(f"Calculating tax for food '{food.name}' priced at {food.price}")


class DiscountCalculator(CalculatorVisitor):
    def visit_book(self, book):
        print(f"Calculating discount for book '{book.title}' by {book.price}")

    def visit_food(self, food):
        print(
            f"Calculating discount for food '{food.name}' priced at {food.price}"
        )


book = Book("The Great Gatsby", 10)
food = Food("Pizza", 15)
tax_calculator = TaxCalculator()
discount_calculator = DiscountCalculator()
book.accept(tax_calculator)
food.accept(tax_calculator)
book.accept(discount_calculator)
food.accept(discount_calculator)
