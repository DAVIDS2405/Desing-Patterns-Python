class CharacterMemento:
    def __init__(self, position, health):
        self.__position = position
        self.__health = health

    @property
    def state(self):
        return {
            'position': self.__position,
            'health': self.__health
        }


class Game:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)
        self.health = 100

    def move(self, x, y):
        self.position = (x, y)

    def take_damage(self, damage):
        self.health -= damage

    def save(self):
        return CharacterMemento(self.position, self.health)

    def restore(self, memento):
        if (memento):
            state = memento.state
            self.position = state['position']
            self.health = state['health']

    def __str__(self):
        return f"Game {self.name}: Position: {self.position}, Health: {self.health}"


class CharacterHistory:
    def __init__(self):
        self.mementos = []

    def save(self, memento):
        self.mementos.append(memento)

    def undo(self):
        if len(self.mementos) > 1:
            self.mementos.pop()
            return self.mementos[-1]
        elif len(self.mementos) == 1:
            self.mementos.pop()
            return None

        return None


character = Game("Hero")
history = CharacterHistory()

print(character, "\n")

history.save(character.save())


character.move(5, 10)
character.take_damage(20)
history.save(character.save())

print(character, "\n")


character.restore(history.undo())

print(character, "\n")
