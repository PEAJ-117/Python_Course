# Example of case of inheritance in real life

# Read, Create, Update, Delete (CRUD) operations for a simple library system

class Model():
    table = False

    def __init__(self):
        if not self.table:
            print("Error, tienes que definir tu tabla")

    def save(self):
        print(f"Guardando la tabla '{self.table}' en la BBDD")

    @classmethod
    def search_id(self, _id):
        print(f"Busqueda por id '{_id}' en la tabla '{self.table}'")


class User(Model):
    table = "Usuario"


user = User()
user.save()
User.search_id(19)
