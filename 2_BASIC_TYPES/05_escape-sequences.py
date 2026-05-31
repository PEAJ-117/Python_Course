# Comentario lineal
# \" -> Para comillas dobles
# \' -> Para comillas simples
# \\ -> Doble pack_slash
# \n -> Salto de linea

# course = "Ultimate "Python"" -> Se considera erroneo
course = 'Ultimate "Python" o'  # Correcto para imprimir strings con comillas dobles
course2 = "Ultimate \"Python 2\" o"  # En otros casos colocar el pack_slash
course3 = "Ultimate \nPython 3"

print(course, course2, course3)
