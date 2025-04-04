from abc import ABC, abstractmethod


class Receiver:
    def open(self):
        print("Open command executed")

    def print(self):
        print("Print command executed")

    def save(self):
        print("Save command executed")


class Command(ABC):
    def __init__(self, receiver: Receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class OpenCommand(Command):
    def execute(self):
        self._receiver.open()


class PrintCommand(Command):
    def execute(self):
        self._receiver.print()


class SaveCommand(Command):
    def execute(self):
        self._receiver.save()


class Invoker:
    def __init__(self, open_command: Command, print_command: Command, save_command: Command):
        self.open_command = open_command
        self.print_command = print_command
        self.save_command = save_command

    def click_open(self):
        self.open_command.execute()

    def click_print(self):
        self.print_command.execute()

    def click_save(self):
        self.save_command.execute()


receiver = Receiver()
open_command = OpenCommand(receiver)
print_command = PrintCommand(receiver)
save_command = SaveCommand(receiver)
invoker = Invoker(open_command, print_command, save_command)

invoker.click_open()
invoker.click_print()
invoker.click_save()
