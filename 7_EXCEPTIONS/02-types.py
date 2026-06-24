# Exception types in Python

try:
    n1 = int(input("Ingrese el primer número: "))
    print(f"El número ingresado es valido: {n1}")

    ndjshd  # NameError: name 'ndjshd' is not defined
    # Output ValueError: invalid literal for int() with base 10: 'abc'
# Manage all exceptions with a generic except block
# except Exception as e: # e \ ex is the variable that will store the exception object

except ValueError as e:
    # print(" Ocurrió un error al convertir el número.\n Asegúrate de ingresar un número válido.")
    # print(type(e))  # <class 'ValueError'>
    print("Ingrese un número válido.")

except NameError as e:
    print("Ocurrió un error")
