from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def __init__(self, user, pwd, url, port):
        self._user = user
        self._pwd = pwd
        self._url = url
        self._port = port

    def send(self, message):
        print(f"Enviando correo electrónico: {message}")

class SMSNotification(Notification):
    def __init__(self, user, pwd):
        self._user = user
        self._pwd = pwd

    def send(self, message):
        print(f"Enviando SMS: {message}")

class NotificationManager:
    def __init__(self, notification: Notification):
        self._notification = notification

    def notify(self, message):
        self._notification.send(message)

email_notification = EmailNotification("usuario", "pwd", "smtp.aws.com", 1212)
sms_notification = SMSNotification("usuario", "contraseña")

notification_manager= NotificationManager(sms_notification)
notification_manager.notify("Un mensaje")