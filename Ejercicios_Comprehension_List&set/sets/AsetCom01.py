#ejemplo 1
lista_original = [3,6,"hola",5]
factor = 2

lista_final = {elem * factor for elem in lista_original}
print(lista_final)

#ejemplo 2

import math
potencias = {math.pow(2,int(elemento)) for elemento in range(8,-4,-1)}
print(potencias)

#ejemplo 3

lista = [4,6,4,12,7]
facto = {math.factorial(elemento) for elemento in lista}
print(facto)