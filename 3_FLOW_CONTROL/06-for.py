# Iterar una lista de elementos
# Buscador
# Op. Matematicas
# Crear una secuencia de numeros con range() que es un iterable

# for number in range(5):
#     # print(number)
#     print(number, number * 'Hola ')

# for else

search = 10
for number in range(5):
    print(number)
    if number == search:
        print("Listo: ", search)
        break  # Detiene el ciclo
else:  # En caso de no cuumplirse
    print("No se encontro")

# Iteracion
print("\nIterando ...\n")
for char in "Ultimate Python":
    print(char)
