
#este programa muestra por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")
