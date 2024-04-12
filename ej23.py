
#este programa muestra por pantalla ordenados de menor a mayor de la lista
awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))