from abc import ABC, abstractmethod

class Target(ABC):
    @abstractmethod
    def payment(self, amount: float):
        pass

class Adaptee:
    def __init__(self):
        self.__connected = False

    def connect(self):
        print("Connecting to the payment system...")
        self.__connected = True

    def pay(self, amount: float):
        if self.__connected:
            print(f"Payment of {amount} processed.")


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.__adaptee = adaptee
    
    def payment(self, amount: float):
        self.__adaptee.connect()
        self.__adaptee.pay(amount)
              
    

def create_order(pay:Target, amount: float):
    pay.payment(amount)
    print(f"Order created with amount: {amount}")
    print("Order created successfully")
    
    
    
adaptee = Adaptee()
adapter = Adapter(adaptee)
create_order(adapter, 100.0)