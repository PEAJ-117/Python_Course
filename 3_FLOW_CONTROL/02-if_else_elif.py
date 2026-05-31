# Comprar una entrada al cine, con pelicula para mayores de 18 con descuento para mayores de 50.
# Las evaluaciones se dan de superior a inferior
# Importante el orden de las condiciones

age = 70
if age > 65:  # Condicion, Si
    print("Puedes ver la pelicula con superdescuento")
elif age > 54:  # Condicion extra, O Si
    print("Puedes ver la pelicula con descuento")
elif age > 17:  # Condicion extra, O Si
    print("Puedes ver la pelicula")
else:  # Condicion, Si No
    print("No puedes entrar")
# print("Ve a otro lado") Identar el codigo para evitar errores

print("Listo")
