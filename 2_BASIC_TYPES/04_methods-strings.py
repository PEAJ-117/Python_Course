# El método es una función que se encuentra dentro de un objeto (POO)

animal = "White Tiger"
print(animal.upper())  # Convierte a mayusculas
print(animal.lower())  # Convierte a minusculas
print(animal.capitalize())  # Primera letra en mayuscula
print(animal.title())  # Primera letra de cada palabra en mayuscula

animal2 = "   Black Panther   "
print(animal2)
print(animal2.strip())  # Borra los espacios
print(animal2.lstrip())  # Borra espacios a la izquierda
print(animal2.rstrip())  # Borra espacios a la derecha

print(animal.find("Ti"))  # Busca y muestra en que pocision esta el caracter
print(animal.find("tI"))  # Si no encuentra lo que busca devuelve -1
print(animal.replace("Whi", "By"))  # Remplaza (string_original, string_nuevo)
print("Wh" in animal)  # Comprueba si existe el caracter con un bool
print("Wh" not in animal)  # Comprueba si no existe el caracter con un bool
