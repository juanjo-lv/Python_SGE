#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Ejemplos de argumentos pasados por valor-copia(dereferencia)
   y por "referencia"'''

def Efuncion1 (uno):
    print ('En funcion1 :',uno, '\tcon tipo: ',type(uno),'\tcon id',id(uno))
    #Modificando
    uno = 3
    print ('En funcion1 modificado:',uno, '\tcon tipo: ',type(uno),'\tcon id',id(uno))

def Efuncion2 (uno):     
    print ('En funcion2 :',uno, '\tcon tipo: ',type(uno),'\tcon id',id(uno))
    #Modificando
    uno = 3
    print ('En funcion2 modificado:',uno, '\tcon tipo: ',type(uno),'\tcon id',id(uno))
    #Reenviando
    return uno
def Efuncion3 (uno):     
    print ('En funcion3 :',uno, '\tcon tipo: ',type(uno),'\tcon id',id(uno))
    #Modificando
    uno = 3
    print ('En funcion3 modificado:',uno, '\tcon tipo: ',type(uno),'\tcon id',id(uno))
    #Reenviando
    return (uno)

#Llamadas----------------------------------------------------------------
var1,var2,var3 = 'UNO', 2, 'Tres'

print('Antes de enviar var1:',var1, '\tcon tipo: ',type(var1),'\tcon id',id(var1)) 
Efuncion1 (var1)# 
print('Despues de enviar var1:',var1, '\tcon tipo: ',type(var1),'\tcon id',id(var1)) 
print()
#devuelta con return 
print('Antes de enviar var1:',var1, '\tcon tipo: ',type(var1),'\tcon id',id(var1)) 
Efuncion2 (var1)# 
print('Despues de enviar var1:',var1, '\tcon tipo: ',type(var1),'\tcon id',id(var1)) 
print()
#devuelta con return 
print('Antes de enviar var1:',var1, '\tcon tipo: ',type(var1),'\tcon id',id(var1)) 
Efuncion3 (var1)# 
print('Despues de enviar var1:',var1, '\tcon tipo: ',type(var1),'\tcon id',id(var1)) 
