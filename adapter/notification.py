from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, sender:str,message: str):
        pass
    
class NotificactionSMS(Notification):
    def send(self,sender:str, message: str):
        print(f"Sending SMS to {sender}: {message}")

class NotificactionEmail():
    def send(self,email:str, message: str,subject:str):
        print(f"Sending Email to {email}: {message} with subject {subject}")    
        
        
class NorificationEmailAdapter(Notification):
    def __init__(self, adaptee: NotificactionEmail,subject:str):
        self.__adaptee = adaptee
        self.__subject = subject
        
    def send(self,sender:str, message: str):
        self.__adaptee.send(sender, message, self.__subject)
        
def create_order(notification: Notification,sender:str,message:str):
    print("Creating order...")
    print("Taxes calculated.")
    print("Payment processed.")
    notification.send(sender,message)


notification = NotificactionSMS()
create_order(notification, "1234567890", "Your order has been created successfully.")

notification = NotificactionEmail()
subject = "Order Confirmation"
adapter = NorificationEmailAdapter(notification, subject)

create_order(adapter,"test@hotmail.com", "Your order has been created successfully.")