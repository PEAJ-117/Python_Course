def suma(a, b):
    res = a + b
    return res


c = suma(1, 2)
d = suma(c, 2)
e = suma(c, d)
print(f'{c} + {d} = {e}')
