
# from abc import ABC, abstractmethod
#
#
# class Model(ABC):
#    @abstractmethod
#    def save(self):
#        pass


# class User(Model):
class User():
    def save(self):
        print("Guardando en la BBDD")


# class Session(Model):
class Session():
    def save(self):
        print("Guardando en la cache")

# Duck Typing


def save(entitys):
    for entity in entitys:
        entity.save()


user = User()
session = Session()

# save(user)
save([session, user])
