#este programa muestra por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")