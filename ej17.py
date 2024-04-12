#este programa muestra por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')