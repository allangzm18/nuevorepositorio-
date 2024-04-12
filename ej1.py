#este programa se debe corregir con continue
u = (1, 2, 3)
v = (4, 5, 6)

def producto_escalar(u, v):
    if len(u) != len(v):
        raise ValueError("Los vectores deben tener la misma longitud")
    return sum(x * y for x, y in zip(u, v))

print(producto_escalar(u, v))

