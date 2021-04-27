#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''Ejemplos de funciones anonimas'''

import F0CaracFun as fu

###Funciones anónimas (lambda) en una sola línea y dentro "expresion"
##print("\n------------------------------------------------------------------")
##print('Funciones anónimas (lambda) en una sola línea y dentro "expresion"')
##print("--------------------------------------------------------------------")
####Función lambda
####----------------------------------------
##print ('La Funcion : ', lambda : print (3 * 4).__name__ ,
##       '\n tipo: ', type(lambda : print (3 * 4)),
##       '\n id: ', id(lambda : print (3 * 4)),
##       '\n docstring: ', lambda : print (3 * 4).__doc__ ,
##       '\n Con las propiedades y metodos:\n', dir(lambda : print (3 * 4)))
##
##fmultiplicar = lambda a, b : print (a * b)
##print ('La Funcion : ', fmultiplicar.__name__ ,
##       '\n tipo: ', type(fmultiplicar),
##       '\n id: ', id(fmultiplicar),
##       '\n docstring: ', fmultiplicar.__doc__ ,
##       '\n Con las propiedades y metodos:\n', dir(fmultiplicar))
##
##fu.caracteristicasFunc(lambda : print (3 * 4), 1)
##
###¿Como invocar/llamar a una función lambda?
###-------------------------------------------
print (lambda : print (3 * 4))# >>> <function <lambda> at 0x04074C00>
print ( (lambda : print (3 * 4)))# >>> <function <lambda> at 0x04074C00>
(lambda : print (3 * 4))# >>> No error, pero no hace nada
lambda : print (3 * 4)# >>> No error, pero no hace nada
###-------------------------------------------
###¿¿Dentro de una expresión, error pues referencia a la misma función??
###-----------------------------------------------------------------
#res_expresion = (lambda : 3 * 4) + 5  #>> TypeError: unsupported operand type(s) for +: 'function' and 'int'
#res_expresion = 5 + ( lambda : 3 * 4  )#TypeError: unsupported operand type(s) for +: 'int' and 'function'
#res_expresion = 5 + int( lambda : 3 * 4  )#TypeError: int() argument must be a string, a bytes-like object or a number, not 'function'
res_expresion = lambda : 3 * 4
print (res_expresion() + 5) #
print (res_expresion() + 5)

### Dandole nombre, asignar nombre
###-----------------------------------------------------------------
##fresultado = lambda : 3 * 4 
##print (fresultado) # <function <lambda> at 0x032D4B70>
##res_expresion = fresultado + 5 # >>> TypeError: unsupported operand type(s) for +: 'function' and 'int'

#funcionA0, y funcionA1
funcionA0 = lambda : print ("HOLA")
funcionA0() # >>> HOLA
funcionA1 = lambda a, b : print (a * b)
print ("Multiplicando: ", funcionA1(3,4)) # >>> 12 >>> Multiplicando:  None
fu.caracteristicasFunc(funcionA1)
#funcionA2, y funcionA3
#funcionA2 = lambda a, b : return (a * b) # sintaxis invalida no admite 'return'
funcionA2 = lambda a, b : a * b
print ('Resultado ', funcionA2(3,4))# >>> Resultado  12
###Ahora ya puede utilizarse dentro de una expresion númerica
print ('Resultado ', funcionA2(3,4) + 5 )# >>> Resultado  17



