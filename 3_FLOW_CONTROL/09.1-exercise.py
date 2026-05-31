msj = """
Operaciones:
suma
resta
multi
div
"""
print()

res = ""

while True:

    if not res:
        res = input("Ingrese numero: ")
        if res.lower() == "salir":
            break
        res = int(res)

    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break

    n2 = input("Ingresa siguiente numero: ")
    if op.lower() == "salir":
        break

    n2 = int(n2)

    if op.lower() == "suma":
        res += n2

    elif op.lower() == "resta":
        res -= n2

    elif op.lower() == "multi":
        res *= n2

    elif op.lower() == "div":
        res /= n2

    else:
        print("Operacion no valida")
        break

    print(f"EL resultado es {res}")
