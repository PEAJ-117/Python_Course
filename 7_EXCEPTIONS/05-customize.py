class MyError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, msj, code):
        self.msj = msj
        self.code = code

    def __str__(self):
        return f"{self.msj} - codigo {self.code}"


def division(n=0):
    if n == 0:
        raise MyError("Error al dividir por 0", 805)
    return 5/n


try:
    division()
except MyError as e:
    print(e)
    print(e.msj)
    print(e.code)
