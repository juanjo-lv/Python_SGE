#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''Ejemplos de funciones con nombre'''
import F0CaracFun as fu

#B)Funciones en una linea "fisica"------------------------------------------------

#def funcionB0(): 'Funcion con docstrig solo' #>>> Correcta se considera el docstring como sentencia
def funcionB0(): 'Funcion con docstrig y pass' ;  pass
def funcionB1(): 'Funcion sin parametros y solo return'; return "Hola Mundo"

#def funcionB2(nombre, mensaje='Hola'): 'Funcion con parametros, llamada a otra función  y sin return' ; print (mensaje, nombre); print (funcionB1())
def funcionB2(nombre, mensaje='Hola'):'Funcion B2' ; print (mensaje, nombre, __doc__ ); print (funcionB1())


def funcionB3(tempC): '''Funcion de Celsiua a Faren'''; return (tempC * 9/5) + 32

#B)Pruebas----------------------------------------------------------------------

print ('\n---------------------------------------------------------')
print ('\r-------B)Funciones con nombre en una linea física--------')
print ('\r---------------------------------------------------------')
print (funcionB0())
fu.caracteristicasFunc(funcionB0,1)
print('---------------')
print (funcionB1())
fu.caracteristicasFunc(funcionB1,1)
print('---------------')
print (funcionB2('buenas','rosa'))
fu.caracteristicasFunc(funcionB2,1)
print ('\n docstring: ', funcionB2.__doc__ )

tempC = 15
print ("Temperatura Celsio: ", tempC ," en Faren... ", funcionB3(tempC )) # > 77
input('Pulsa')
