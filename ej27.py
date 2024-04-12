#El programa muestra  todo lo que el usuario introduzca hasta que el usuario escriba “salir”  terminará.
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)