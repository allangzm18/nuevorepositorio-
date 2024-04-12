#este programa pide una frase y luego la letra que queremos minuscula y la muestra mayuscula
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))