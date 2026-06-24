import os
from pathlib import Path
import sys

# print(sys.argv)


def clix(args):
    if len(args) == 1:
        print("Sin argumentos")
        return
    if len(args) != 3:
        print("Necesito 2 argumentos")
        return

    originx = args[1]
    o = Path(originx)
    if not o.exists():
        print("Origen no existe")
        return

    destx = args[2]
    d = Path(destx)
    if d.exists():
        print("El destino no puede existir")
        return

    os.rename(str(originx), str(destx))
    print("El archivo fue renombrado con exito")


clix(sys.argv)
