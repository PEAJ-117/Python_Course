class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def speak(self):
        print(f"{self.__name, self.__age} dice: Hooola!!!")

    @classmethod
    def factory(cls):
        return cls("Ritcher", 26)


person1 = Person.factory()
person1.speak()
print(person1.get_name())
print(person1.__dict__)
