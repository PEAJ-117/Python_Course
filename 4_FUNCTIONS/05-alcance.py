saludo = "Hola global"


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaAsi():
    saludo = 24
    print(saludo)


print(saludo)
saludar()
print(saludo)

# Variables globales son malas practicas
