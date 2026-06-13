"""Module providing a function printing python version."""

from abc import ABC, abstractmethod


class Model(ABC):
    # table = False

    # def __init__(self):
    #    if not self.table:
    #        print("Error, tienes que definir tu tabla")

    @property
    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def save(self):
        # print(f"Guardando la tabla '{self.table}' en la BBDD")
        pass

    @classmethod
    def search_id(self, _id):
        print(f"Busqueda por id '{_id}' en la tabla '{self.table}'")


class User(Model):
    table = "Usuario"

    def save(self):
        print("Guardando usuario")


user = User()
user.save()
User.search_id(19)
