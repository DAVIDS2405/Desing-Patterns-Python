from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, balance: float):
        self._balance = balance

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Deposited {amount}. New balance is {self._balance}")

    def withdraw(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}")
        else:
            print("Insufficient funds")


class Command(ABC):
    def __init__(self, account: Account):
        self._account = account

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class DepositCommand(Command):
    def __init__(self, account: Account, amount: float):
        super().__init__(account)
        self.__amount = amount

    def execute(self):
        self._account.deposit(self.__amount)

    def undo(self):
        self._account.withdraw(self.__amount)


class WithdrawCommand(Command):
    def __init__(self, account: Account, amount: float):
        super().__init__(account)
        self.__amount = amount

    def execute(self):
        self._account.withdraw(self.__amount)

    def undo(self):
        self._account.deposit(self.__amount)


class TransactionManager:
    def __init__(self):
        self.__commands = []

    def execute_command(self, command: Command):
        command.execute()
        self.__commands.append(command)

    def undo_last_command(self):
        if self.__commands:
            command = self.__commands.pop()
            command.undo()
        else:
            print("No commands to undo")


account = Account(100)
transaction_manager = TransactionManager()
deposit_command = DepositCommand(account, 50)
withdraw_command = WithdrawCommand(account, 30)


transaction_manager.execute_command(deposit_command)
transaction_manager.execute_command(deposit_command)
transaction_manager.execute_command(withdraw_command)

transaction_manager.undo_last_command()
transaction_manager.undo_last_command()
