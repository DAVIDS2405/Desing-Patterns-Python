from abc import ABC, abstractmethod

class HtmlForm:
    def __init__(self, action, method, fields):
        self.action = action
        self.method = method
        self.fields = fields

    def __str__(self):
        fields_html = "\n".join(self.fields)
        return f"""
                <form action="{self.action}" method="{self.method}">
                    {fields_html}
                </form>
                """
    
class Builder(ABC):
    @abstractmethod
    def set_action(self, action):
        pass

    @abstractmethod
    def set_method(self, method):
        pass

    @abstractmethod
    def add_text_input(self, name, placeholder):
        pass

    @abstractmethod
    def add_password_input(self, name, placeholder):
        pass

    @abstractmethod
    def add_email_input(self, name, placeholder):
        pass

    @abstractmethod
    def add_submit_button(self, value):
        pass

    @abstractmethod
    def build(self):
        pass

class HtmlFormBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.action = ""
        self.method = "POST"
        self.fields = []
        return self
    
    def set_action(self, action):
        self.action = action
        return self
    
    def set_method(self, method):
        self.method = method
        return self
    
    def add_text_input(self, name, placeholder):
        field = f'<input type="text" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self
    
    def add_password_input(self, name, placeholder):
        field = f'<input type="password" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self
    
    def add_email_input(self, name, placeholder):
        field = f'<input type="email" name="{name}" placeholder="{placeholder}">'
        self.fields.append(field)
        return self
    
    def add_submit_button(self, value="Enviar"):
        field = f'<button type="submit">{value}</button>'
        self.fields.append(field)
        return self
    
    def build(self):
        form = HtmlForm(self.action, self.method, self.fields)
        self.reset()
        return form
    

class FormDirector:
    def __init__(self, builder: Builder):
        self.builder = builder

    def create_login(self):
        (self.builder.set_action("/login")
              .set_method("POST")
              .add_email_input("email", "Correo")
              .add_password_input("pass","Contraseña")
              .add_submit_button())
        return self.builder.build()
    
    def create_register(self):
        (self.builder.set_action("/register")
         .set_method("POST")
         .add_text_input("name","Nombre")
         .add_email_input("email", "Correo")
         .add_password_input("pass", "Contraseña")
         .add_password_input("confirm_pass", "Vuelve a escribir tú contraseña")
         .add_submit_button("Registrar"))
        return self.builder.build()


html_form_builder = HtmlFormBuilder()

login_form = (html_form_builder.set_action("/login")
              .set_method("POST")
              .add_email_input("email", "Correo")
              .add_password_input("pass","Contraseña")
              .add_submit_button()
              .build()
              )

print(login_form)

director = FormDirector(html_form_builder)
login = director.create_login()
register = director.create_register()

print(login)
print(register)