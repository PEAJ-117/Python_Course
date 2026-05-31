# Codificar una calculadora iterativa
# El usuario debe ingresar el numero
# Despues la operacion y luego el numero siguiente

msj = """
Bienvenido a PyLator.
Operaciones basicas disponibles:
a) Sumar
b) Restar
c) Multiplicar
d) Dividir
x) Salir
"""
print(msj)

while True:

    command = input("W$ ")

    if command.lower() == "a":
        print("Has elegido suma.")
        n1 = int(input("#1 "))
        n2 = int(input("#2 "))
        res = n1 + n2
        print(res)

    elif command.lower() == "b":
        print("Has elegido resta.")
        n1 = int(input("#1 "))
        n2 = int(input("#2 "))
        res = n1 - n2
        print(res)

    elif command.lower() == "c":
        print("Has elegido multiplicacion.")
        n1 = int(input("#1 "))
        n2 = int(input("#2 "))
        res = n1 * n2
        print(res)

    elif command.lower() == "d":
        print("Has elegido division.")
        n1 = int(input("#1 "))
        n2 = int(input("#2 "))
        res = n1 / n2
        print(int(res))

    elif command.lower() == "x":
        break

    else:
        print("Seleccione una operacion valida")

print("<<< Proceso terminado >>>")
