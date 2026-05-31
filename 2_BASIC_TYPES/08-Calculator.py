# Obtener datos del usario
n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
div = n1 / n2

msj = f"""
Para los numeros {n1} y {n2},
Suma = {suma}.
Resta = {resta}.
Producto = {mult}.
Division = {div}.
"""
print(msj)
# print("Numeros ingresados: ", n1, "y", n2)
# print("El resultado de la suma es: ", n1 + n2)
