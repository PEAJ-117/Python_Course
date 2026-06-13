# messaje = "Welcome to world of Python"
# print(type(messaje))
# <class 'str'>

# Clase: Plano de construccion de objetos, define atributos y comportamientos comunes a todos los objetos de ese tipo.
# Objeto: Instancia concreta de una clase, con sus propios valores para los atributos y comportamientos definidos por la clase.

class Person:
    # Variables de clase: Variable que pertenece a la clase en sí, compartida por todas las instancias de esa clase.
    eyes = 2

    # CONSTRUCTOR: Metodo especial que se llama automaticamente al crear una instancia de la clase, se utiliza para inicializar los atributos del objeto.
    # __init__ palabra reservada para el constructor, self referencia a la instancia , valores del constructor
    def __init__(self, name, age):
        # Propiedades: Variable que pertenece a un objeto, se utiliza para almacenar datos relacionados con ese objeto.
        self.name = name
        self.age = age

    # Metodo de clase

    @classmethod  # Transforma el metodo a uno propio para la clase
    # Metodo: Funcion definida dentro de una clase, describe el comportamiento de los objetos de esa clase.
    def speak(cls):  # Se cambia de self a cls, esto se utiliza para metodos de clase para referirse a la clase misma
        # print(f"{self.name} speak: Hello, I am a person.")
        print("Hooola!!!")  # Se acorta la sintaxis

    # Method Factory

    @classmethod
    def factory(cls):
        return cls("Ritcher", 26)


# Person.speak()
person1 = Person("John", 54)
person2 = Person("Mia", 34)
person3 = Person("Karen", 18)
person4 = Person.factory()

print(person4.age, person4.name)

# Person.eyes = 4
# my_friend = Person("Alice", 18)
# my_friend.eyes = 8
# my_friend2 = Person("Andy", 5)
#
# print(Person.eyes)
# print(my_friend.eyes)
# print(my_friend2.eyes)

# my_friend.speak()
# print(my_friend.name)  # Alice, accede al atributo name del objeto my_friend
# print(my_friend2.name)

# ------------------------------------------------
# print(type(my_friend))  # <class '__main__.Person'>
# Llamada al metodo speak del objeto my_friend, imprime: Hello, I am a person.
# my_friend.speak()
# # True, verifica que my_friend es una instancia de la clase Person
# print(isinstance(my_friend, Person))
# # False, my_friend no es una instancia de str
# print(isinstance(my_friend, str))
