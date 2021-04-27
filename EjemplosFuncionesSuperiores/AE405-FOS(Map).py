#! /usr/bin/env python
# -*- coding: utf-8 -*-
'Ejemplo Funcion de orden superior: map '
# map(nom_función,iterable/iterador [, iterable/iteradore]...

#Ejemplo 0
#--------------------------------------------------------------------##
#lista1 = ["a","b"] ;lista2 = [1,2,3]
#print(list( map(None, lista1,lista2)))
 #TypeError: 'NoneType' object is not callable
 ###Esto ya no funciona, solo en python2

##Ejemplo 1
##--------------------------------------------------------------------##
'''
def A_mayusculas(iterable):
    return iterable.upper()

#Pruebas------------------------------------------------------------------
cadena = "me tienes hasta l@s iterables"
tupla = ("me","tienes","hasta","l@s","iterables")
resultado = list( map(A_mayusculas,cadena))
resultado = list( map(A_mayusculas,tupla))
print (resultado)
'''

##Ejemplo 2
##--------------------------------------------------------------------##
'''
def tipoylen(iterable):
    retorno =  '\nEl ' + str(iterable)+ ' tipo ' + str(type(iterable))
    if '__len__' in dir(iterable): retorno += ' len ' + str(len(iterable))
    return retorno

#Pruebas------------------------------------------------------------------
tupla0 = ('melon', 559, 'sandia', 'rojo')
print ('La tupla es: ', tupla0 )
retornado = map(tipoylen, tupla0 ) #<map object at 0x030681F0>
print('Los valores retornados son :' )
for elem in retornado:
    print (elem)
'''
##Ejemplo 3a
##--------------------------------------------------------------------##
'''
def suma0(elem_iterable1, elem_iterable2):
    return print ('La suma de ' , elem_iterable1, ' y ' , elem_iterable2, ' es ', elem_iterable1 + elem_iterable2)
#Pruebas------------------------------------------------------------------
lista1 = [5, 12, -5, 18, 0, -24, 32]
lista2 = [3, 15,  5, 10, 20, 15, 32]
print ('Numeros1     \t', lista1 )
print ('Numeros2     \t', lista2 )
print ('\r-------------------------------------------------------------------')
print ("\rLa suma es:\t", list(map(suma0,lista1 ,lista2 ))) 
'''
##Ejemplo 3b
##--------------------------------------------------------------------##
'''
def suma1(elem_iterable1, elem_iterable2):
      return ( elem_iterable1 + elem_iterable2)
#Pruebas------------------------------------------------------------------
lista1 = [5, 12, -5, 18, 0, -24, 32]
lista2 = [3, 15,  5, 10, 20, 15, 32]
print ('Numeros1     \t', lista1 )
print ('Numeros2     \t', lista2 )
print ('\r-------------------------------------------------------------------')
print ("\rLa suma es:\t", list(map(suma1,lista1 ,lista2 ))) 
