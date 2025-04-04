from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, issues, next=None):
        self._issues = issues
        self._next = next

    @abstractmethod
    def handle(self, issue):
        pass


class Level1Support(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Level 1 Support: Handling issue '{issue}'")
        elif self._next:
            print(f"Level 1 Support: Passing issue '{issue}' to next level")
            self._next.handle(issue)


class Level2Support(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Level 2 Support: Handling issue '{issue}'")
        elif self._next:
            print(f"Level 2 Support: Passing issue '{issue}' to next level")
            self._next.handle(issue)


class SupportManager(Handler):
    def handle(self, issue):
        if issue in self._issues:
            print(f"Support Manager: Handling issue '{issue}'")
        elif self._next:
            print(f"Support Manager: Passing issue '{issue}' to next level")
            self._next.handle(issue)


manager = SupportManager([])
level2 = Level2Support(["bug", "user_delete", "exception"], manager)
chain = Level1Support(["user_create", "password_reset"], level2)

chain.handle("bug")
