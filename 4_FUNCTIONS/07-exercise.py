# Definir una funcion que reciba cierto parametro
# La funcion identifica el Palindromo
# El Palindromo es un texto igual ya sea de manera continua o invertida

# Eliminar los espacios en blanco de un string
# Aplicar reversa al string con for

def no_space(text):  # Funcion que recibe el texto
    new_text = ""  # Crear nuevo texto
    for char in text:
        if char != " ":  # char es distinto de un string vacio
            new_text += char  # Concatenar cada caracter a menos que sea un espacio en blanco
    return new_text


def reverse(text):  # Funcion del string en reverse
    reverse_text = ""  # Variable vacio
    for char in text:
        reverse_text = char + reverse_text  # Da vuelta al string
    return reverse_text


def palindromo(text):  # Funcion principal
    text = no_space(text)  # Funcion para eliminar espacios en blanco
    reverse_text = reverse(text)
    # return text == reverse_text
    return text.lower() == reverse_text.lower()  # Correccion para mayusculas


print(palindromo("Amo la paloma"))
print(palindromo("Hola Mundo"))
print(palindromo("RECONOCER"))
print(palindromo("Somos o No Somos"))
