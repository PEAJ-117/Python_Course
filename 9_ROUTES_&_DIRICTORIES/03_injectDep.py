from pathlib import Path
import db
import graphql
import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dep = {
    "db": db,
    "api": api,
    "graphql": graphql
}


def load(p):
    package = __import__(str(p).replace("/", "."))
    try:
        package.init(**dep)
    except ():
        print("Paquete sin funcion init")


list(map(load, paths))
