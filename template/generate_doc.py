from abc import ABC, abstractmethod


class DocumentTemplate(ABC):

    @abstractmethod
    def add_header(self):
        pass

    @abstractmethod
    def add_content(self):
        pass

    @abstractmethod
    def add_footer(self):
        pass

    def generate(self, file_name):
        with open(file_name, 'w') as file:
            file.write(self.add_header())
            file.write("\n\n")
            file.write(self.add_content())
            file.write("\n\n")
            file.write(self.add_footer())
        print(f"Document {file_name} generated successfully.")


class SimpleDocument(DocumentTemplate):

    def add_header(self):
        return "Header: Simple Document"

    def add_content(self):
        return "This is a simple document content."

    def add_footer(self):
        return "Footer: Simple Document"


class MarkdownDocument(DocumentTemplate):

    def add_header(self):
        return "# Header: Markdown Document"

    def add_content(self):
        return "This is a **markdown** document content."

    def add_footer(self):
        return "Footer: Markdown Document"


simple = SimpleDocument()
simple.generate("simple_document.txt")

markdown = MarkdownDocument()
markdown.generate("markdown_document.md")
