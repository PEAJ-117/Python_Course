# Suponiendo que se tiene un numero igual a uno
# y duplicarlo cuando sea menor o igual a 7

number = 1

while number < 100:
    print(number)
    number *= 2

# Haremos un loop en donde
# Mientras se ingrese algo diferente
# Seguira ejecutandose
print("\n-----Loop-------\n")

command = ""
while command.lower() != "salir":
    command = input("$> ")
    print(command)

# Loop Infinito
# Cunaod no haiga una condicion de salida
print("\n------Loop Infinito------\n")


while True:
    command = input("$> ")
    print(command)
    # Necesario colocar para evitar el consumo y cierre forzado
    if command.lower() == "salir":
        break
