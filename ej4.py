
#este programa necesita saber si la persona es mayor a 16 para saber si atributa a un impuesto si en caso es menor entonces no tributa
age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")