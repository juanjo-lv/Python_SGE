#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Ejemplos de funciones con nombre'''

import F0CaracFun as fu

#A)Funciones en varias lineas------------------------------------------------

def funcionA0():
    'Funcion con docstrig y pass'
    pass

def funcionA1():
    'Funcion sin parametros y solo return'
    return "Hola Mundo"

def funcionA2(nombre, mensaje='Hola'): #Parametro  por defecto
    '''Funcion con parametros,
       llamada a otra función  y sin return'''
    print (mensaje, nombre) 
    print (funcionA1())         #Llamada a otra funcion
    '''fin funcion saludar'''   # No tiene efecto para __doc__

#A)Pruebas----------------------------------------------------------------------

print ('\n-------------------------------------------------------')
print ('\r-------A)Funciones con nombre en varias lineas---------')
print ('\r-------------------------------------------------------')
print (funcionA0())
fu.caracteristicasFunc(funcionA0,1)
print('')
input('Pulsa')
print (funcionA1())
fu.caracteristicasFunc(funcionA1,1)
print('')
#fu.caracteristicasFunc(funcionA1())#error
input('Pulsa')
print (funcionA2('buenas','rosa'))
fu.caracteristicasFunc(funcionA2,1)
input('Pulsa')
