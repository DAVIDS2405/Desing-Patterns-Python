from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, message: str, sender: str):
        pass


class ChatMediator(Mediator):
    def __init__(self, log):
        self.__participants = []
        self._log = log
        self._log.set_mediator(self)

    def register(self, participant):
        self.__participants.append(participant)

    def notify(self, message: str, sender: str):
        self._log.receive(message)
        for participant in self.__participants:
            if participant.name != sender:
                participant.receive(message)


class Participant:
    def __init__(self, name: str, mediator: Mediator):
        self.name = name
        self._mediator = mediator
        self._mediator.register(self)

    def send(self, message: str):
        print(f"{self.name} sends: {message}")
        self._mediator.notify(message, self.name)

    def receive(self, message: str):
        print(f"{self.name} receives: {message}")


class Log:
    def __init__(self, log_file):
        self.__log_file = log_file
        self.__mediator = None

    def set_mediator(self, mediator):
        self.__mediator = mediator

    def send(self, message: str):
        print(f"Log: {message}")
        self.__mediator.notify(message, self)

    def receive(self, message: str):
        with open(self.__log_file, 'a') as f:
            f.write(f"{message}\n")


log = Log("chat_log.txt")
mediator = ChatMediator(log)
participant1 = Participant("Alice", mediator)
participant2 = Participant("Bob", mediator)
participant3 = Participant("Charlie", mediator)

participant1.send("Hello, everyone!")
print("")
participant2.send("Hi, Alice!")
print("")
participant3.send("Hey, Alice and Bob!")

log.send("This is a log message.")
