#! /usr/bin/env python
# -*- coding: utf-8 -*-
'Ejemplo Funcion de orden superior: filter '
# ('filter(nom_función, iterable/iterador)')

#Ejemplo 1
#--------------------------------------------------------------------##
'''
def pares(numero): return numero % 2

#Pruebas------------------------------------------------------------------
limite = 11
#Filtrando los números que son pares (multiplos de 2)
print(list(filter(pares,range(limite))))

# Con una comprehension list
print([elem for elem in range(limite) if pares(elem)])
'''
#Ejemplo 1B --> Comprobar el funcionamiento con None
#Ejemplo 2B --> Mejorar para según el caso limitar por pares,  impares, o multiplo de X

#Ejemplo 2
#--------------------------------------------------------------------##
'''
def mayor_que(elem_iterable, num=0):    
    return  False if (elem_iterable < num) else True

#Pruebas------------------------------------------------------------------
numeros = [5, 12, -5, 18, 0, -24, 32]
print (numeros)

print(list(filter(mayor_que, numeros)))
print(list(filter(mayor_que, iter(numeros))))
 '''
#Ejemplo 2B --> Mejorar para indicar el número con quien comparar





