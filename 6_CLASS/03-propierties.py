class Person:
    def __init__(self, name):
        self.name = name

    @property  # Solo para funciones GET
    def name(self):
        print("way for getter")
        return self.__name

    @name.setter
    def name(self, name):
        print("way for setter")
        if name.strip():
            self.__name = name
        return


person = Person("Shaggy")
print(person.name)
