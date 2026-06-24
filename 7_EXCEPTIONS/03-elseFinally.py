try:
    n1 = int(input("Ingrese el primer número: "))

# Output ValueError: invalid literal for int() with base 10: 'abc'
except Exception as e:
    print("Asegúrate de ingresar un número válido.")

else:  # When there are no exceptions
    print("Sin errores")

finally:  # Use in case have success o failure
    print("Se ejecuta siempre")
