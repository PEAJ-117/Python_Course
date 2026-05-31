# Las comillas dobles nos imprime texto plano y limitado
name_course = "Ultimate Python..."

# Las comiilas triples nos imprime un texto extenso
description_course = """
Ultimate Python,
This course content all details you need learn to found work as programmer.
Thanks you attention.
"""

print(name_course, description_course)

# Obtener la longitud de un string con la función len()
print(len(name_course))
# Acceder a un caracter, colocar el indice "n" dentro de llaves cuadradas
print(name_course[0])
# Cortar el string [inicio:final]
print(name_course[0:8])
# El indice final esta por defecto, hasta donde termine
print(name_course[9:])
# El indice inicial esta por defecto, inicia de 0
print(name_course[:8])
# Por defecto los indices son considerados de cero al final
print(name_course[:])
