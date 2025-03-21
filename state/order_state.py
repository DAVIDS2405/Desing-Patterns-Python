from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def pay(self, order):
        pass

    @abstractmethod
    def ship(self, order):
        pass

    @abstractmethod
    def deliver(self, order):
        pass


class NewOrderState(OrderState):
    def pay(self, order):
        print("¡El pedido se ha pagado con éxito!")
        order.set_state(PaidOrderState())

    def ship(self, order):
        print("No se puede enviar sin estar pagado")

    def deliver(self, order):
        print("No se puede entregar sin estar pagado")

class PaidOrderState(OrderState):
    def pay(self, order):
        print("El pedido ya ha sido pagado")

    def ship(self, order):
        print("¡El pedido ha sido enviado con éxito!")
        order.set_state(ShippedOrderState())

    def deliver(self, order):
        print("No se puede entregar sin estar enviado")

class ShippedOrderState(OrderState):
    def pay(self, order):
        print("El pedido ya ha sido pagado")

    def ship(self, order):
        print("El pedido ya ha sido enviado")

    def deliver(self, order):
        print("¡El pedido ha sido entregado con éxito!")
        order.set_state(DeliveredOrderState())

class DeliveredOrderState(OrderState):
    def pay(self, order):
        print("El pedido ya ha sido pagado")

    def ship(self, order):
        print("El pedido ya ha sido enviado")
        
    def deliver(self, order):
        print("El pedido ya ha sido entregado")

class Order:
    def __init__(self, state: OrderState):
        self.state = state

    def set_state(self, state: OrderState):
        self.state = state

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)
    
    def deliver(self):
        self.state.deliver(self)


order = Order(NewOrderState())

order.ship()   
order.deliver()   

order.pay()
order.ship()      
order.deliver()  

order.pay()