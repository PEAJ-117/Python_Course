def division(n=0):
    if n == 0:
        raise ZeroDivisionError("Error al dividir por 0,")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)

# Avoid throwing exceptions too often, due to performance consumptio
