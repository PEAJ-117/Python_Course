try:
    n1 = int(input("Ingrese el primer número: "))
    print(f"El número ingresado es valido: {n1}")
    # Output ValueError: invalid literal for int() with base 10: 'abc'
except:
    print(" Ocurrió un error al convertir el número.\n Asegúrate de ingresar un número válido.")
