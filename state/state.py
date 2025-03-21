from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class ProcessContext:
    def __init__(self, state: State):
        self._state = state

    def set_state(self, state: State):
        self._state = state

    def request(self):
        self._state.handle(self)

class StartState(State):
    def handle(self, context: ProcessContext):
        print("Estado: Inicial. Pasando a ejecución")
        context.set_state(RunState())

class RunState(State):
    def handle(self, context: ProcessContext):
            print("Estado: Ejecutando. Pasando a finalizado")
            context.set_state(EndState())
    
class EndState(State):
    def handle(self, context: ProcessContext):
            print("Estado: Finalizado.")


process = ProcessContext(StartState())

process.request()
process.request()
process.request()
process.request()
        