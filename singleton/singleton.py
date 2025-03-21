class Singleton:
    _instance = None

    def __new__(cls, name = None, age = None):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.name = name
            cls._instance.age = age
        return cls._instance
    
singleton1 = Singleton("Héctor", 30)
singleton2 = Singleton()

print(singleton1 is singleton2)
print(singleton2.name)
print(singleton1.name)