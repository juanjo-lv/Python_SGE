#! /usr/bin/env python
# -*- coding: utf-8 -*-
'Ejemplos Funciones de orden superior en Modulo'

##Ejemplo 1
##--------------------------------------------------------------------##
#functools.reduce(nom_función, iterable[,inicio])
'''
import functools
def multiplicar(x, y):
    print("Parcial : de ", x , " x ", y, ' = ', x * y)
    return x * y
###Pruebas------------------------------------------------------------------
lista = [1, 2, 3, 4]
print ('Lista original: ', lista)
valor = functools.reduce(multiplicar, lista)
print('El final es : ', valor)  # El final es :  24
print('\r-----------------------------------------------')
inicio = 5
print('\rAhora empezando por...', inicio)
valor = functools.reduce(multiplicar, lista,inicio)
print('El final es : ', valor)  # El final es :  
print('\r-----------------------------------------------')
print('\rCon funciones lambda')
print ('-----------------------------------------------')
print( functools.reduce((lambda x, y: x * y), lista))
print('El final es : ', functools.reduce((lambda x, y: x * y), lista,inicio))
print ('-----------------------------------------------')
print ('Este codigo hace lo mismo que la función reduce')
lista = (1, 2, 3, 4)
#product = 1
product = 5
for num in lista:
    product = product * num
print ("Resultado: ", product) # product = 24 /120
print ('-----------------------------------------------')
'''
##Ejemplo 2 
##--------------------------------------------------------------------##
''' 
import functools
import operator
import itertools
###Pruebas------------------------------------------------------------------
print(functools.reduce(operator.concat,["ber","ber","echos"],"comer "))
#Diferentes formas de hacer lo mismo
print(functools.reduce(operator.add,[1,2,3,4]))
print ("----------------")
print(sum([1,2,3,4]))
print ("----------------")
for elemento in itertools.accumulate([1,2,3,4]):
    print(elemento)
'''    


