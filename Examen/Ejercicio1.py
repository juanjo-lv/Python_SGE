#Ejercicio 1 apartado a
lista1 = [a for a in range(20) if a%2 !=0]
print(lista1)

lista2 = [b for b in range(20) if b%3==0]
print(lista2)

lista3 = [c for c in range(20) if c%2 != 0 and c%3==0]
print(lista3)

#Ejercicio 1 apartado b
lista4 = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
diccionario ={(a+1):b.capitalize() for a,b in zip(range(len(lista4)),lista4)}
print(diccionario)