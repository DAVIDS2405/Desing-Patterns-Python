from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self,  event: str):
        pass


class BaseComponent(ABC):
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator


class ComponentA(BaseComponent):
    def hi(self):
        print("Component A: Hi")
        self._mediator.notify("A")

    def response(self):
        print("Component A: Response")


class ComponentB(BaseComponent):
    def hi(self):
        print("Component B: Hi")
        self._mediator.notify("B")

    def response(self):
        print("Component B: Response")


class ConcreteMediator(Mediator):
    def __init__(self, component_a, component_b):
        self._component_a = component_a
        self._component_b = component_b

        self._component_a.set_mediator(self)
        self._component_b.set_mediator(self)

    def notify(self, event: str):
        if event == "A":
            print("Mediator: Notifying Component B")
            self._component_b.response()
        elif event == "B":
            print("Mediator: Notifying Component A")
            self._component_a.response()


component_a = ComponentA()
component_b = ComponentB()
mediator = ConcreteMediator(component_a, component_b)
component_a.hi()
component_b.hi()
