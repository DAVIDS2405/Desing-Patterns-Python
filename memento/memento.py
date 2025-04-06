class Memento:
    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state


class Caretaker:
    def __init__(self):
        self.__history = []

    def save(self, memento):
        self.__history.append(memento)

    def undo(self):
        if len(self.__history) > 0:
            self.__history.pop()
            return self.__history[-1]
        elif len(self.__history) == 1:
            self.__history.pop()
            return None
        else:
            return None


class Originator:
    def __init__(self):
        self.__text = ""

    def append(self, new_text):
        self.__text += new_text

    def save(self):
        return Memento(self.__text)

    def restore(self, memento: Memento):
        if memento:
            self.__text = memento.state
        else:
            self.__text = ""

    @property
    def text(self):
        return self.__text


editor = Originator()
historic = Caretaker()

editor.append("Hi ")
historic.save(editor.save())

editor.append("Hello World ")
historic.save(editor.save())

editor.append("hi World!")
historic.save(editor.save())

print(editor.text)

editor.restore(historic.undo())
print(editor.text)
