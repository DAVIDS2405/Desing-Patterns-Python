class Stock:
    def check(self,concepts)->bool:
        return True


class Payment:
    def pay(self,customer_id,concepts):
        print("Payment ok")


class Email:
    def send(self,customer_id):
        print("Email sent")


class Facade:
    def __init__(self):
        self.__stock = Stock()
        self.__payment = Payment()
        self.__email = Email()


    def create_payment(self,customer_id,concepts):
        if self.__stock.check(concepts):
            self.__payment.pay(customer_id,concepts)
            self.__email.send(customer_id)
        else:
            print("Payment failed")

concepts = [
    {"id": 1, "name": "product1", "price": 10},
    {"id": 2, "name": "product2", "price": 20},
    {"id": 3, "name": "product3", "price": 30},
    {"id": 4, "name": "product4", "price": 40},
    {"id": 5, "name": "product5", "price": 50},
]

facade =  Facade()
facade.create_payment(1,concepts)
