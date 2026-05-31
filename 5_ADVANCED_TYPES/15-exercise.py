from pprint import pprint

# 1. COMPRENSION DE LISTAS: Crear una funcion para eliminar los  espacios en blanco de un string y devolver una lista con los caracteres restantes

string = "Espaacios en blaanco"


def spaceRem(text):
    return [char for char in text if char != " "]


notSpaces = spaceRem(string)
# print(notSpaces)

# 2. Contar en un diccionario el numero de veces que aparece cada caracter en un string


def countChars(list):
    chars_dict = {}  # Creamos un diccionario vacio para almacenar los caracteres y su contador
    for char in list:  # Iteramos sobre cada caracter en la lista
        if char in chars_dict:  # Si el caracter ya esta en el diccionario, incrementamos su contador
            chars_dict[char] += 1
        else:  # Si el caracter no esta en el diccionario, lo agregamos con un contador de 1
            chars_dict[char] = 1
    return chars_dict  # Devolvemos el diccionario con los caracteres y su contador


counted = countChars(notSpaces)
# pprint(counted, width=1)

# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contenga tuplas [("a", 3) ...]


def order(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )


orders = order(counted)
# print(orders)
# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor


def maxTuples(list):
    # Obtenemos el valor de la primera tupla como referencia
    max_value = list[0][1]
    max_tuples = []  # Creamos una lista vacia para almacenar las tuplas con el mayor valor
    for tuple in list:  # Iteramos sobre cada tupla en la lista
        # Si el valor de la tupla es igual al valor maximo, la agregamos a la lista de tuplas maximas
        if tuple[1] == max_value:
            max_tuples.append(tuple)
        else:  # Si el valor de la tupla es menor al valor maximo, rompemos el ciclo ya que las tuplas estan ordenadas de mayor a menor
            break
    return max_tuples  # Devolvemos la lista de tuplas con el mayor valor


max_tuples = maxTuples(orders)
# print(max_tuples)

# 5. Crear un mensaje que diga:
# Los caracteres que mas se repiten con N repeticiones son:
# -a
# -b


def createMessage(list):
    message = f"Los caracteres que mas se repiten con {list[0][1]} repeticiones son:\n"
    for tuple in list:
        message += f"-{tuple[0]}\n"
    return message


print(createMessage(max_tuples))
