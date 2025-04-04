from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next=None):
        self._next = next

    @abstractmethod
    def handle(self, request):
        pass


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Executing A")
        elif self._next:
            print("Passing to next handler")
            self._next.handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Executing B")
        elif self._next:
            print("Passing to next handler")
            self._next.handle(request)


class ConcreteHandlerDefault(Handler):
    def handle(self, request):
        print("Default handler executed")


concreteHanderDefault = ConcreteHandlerDefault()
concreteHandlerB = ConcreteHandlerB(ConcreteHandlerDefault)


chain = ConcreteHandlerA(concreteHandlerB)
chain.handle("A")
