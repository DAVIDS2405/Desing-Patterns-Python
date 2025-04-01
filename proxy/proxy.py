from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def action(self):
        pass


class RealSubject(Subject):
    def action(self):
        print("Realizar accion")

class Proxy(Subject):
    def __init__(self,real_subject:RealSubject):
        self.__real_subject = real_subject
        self.__authorized = False

    def action(self):
        if self.__authorized:
            print("Proxy: acceso permitido")
            self.__real_subject.action()
        else:
            print("Proxy:Acceso no permitido")

    def login(self,user:str,password:str):
        if user == "user" and password == "123":
            self.__authorized = True


def some (subject:Subject):
    subject.action()

real_subject = RealSubject()

proxy = Proxy(real_subject)
proxy.login("user","123")
some(proxy)
