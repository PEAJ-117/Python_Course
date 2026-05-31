name = "Paul Edwin"
lastname = "Antonio Juan"
# Formato no recomendado
nameComplete = name + " " + lastname
# Formato recomendado f" y F"
nameComplete2 = f"{name} {lastname}"
nameComplete3 = F"{name} {lastname}"
# Indice y suma
nameComplete4 = f"{name[0]} {2 + 5}"
print(nameComplete)
print(nameComplete2)
print(nameComplete3)
print(nameComplete4)
