from abc import ABC, abstractmethod

class Text(ABC):
    @abstractmethod
    def print(self):
        pass


class SimpleText(Text):
    def __init__(self, content):
        self._content = content

    def print(self):
        return self._content
    
    
class TextDecorator(Text):
    def __init__(self, text: Text):
        self._text = text 
    
    def print(self):
        return self._text.print()
    
class BoldText(TextDecorator):
    def print(self):
        return f"<b>{self._text.print()}</b>"

    
class ItalicsText(TextDecorator):
    def print(self):
        return f"<i>{self._text.print()}</i>"
    
class UnderlinedText(TextDecorator):
    def print(self):
        return f"<u>{self._text.print()}</u>"
    
text = SimpleText("Hola mundo")
bold = BoldText(text)
italics = ItalicsText(bold)
underlined = UnderlinedText(italics)

print(underlined.print())