#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Argumentos a Parametros por posición'''

def EXPosicion1 (uno, dos, tres):
    'Argumentos a parametros por posicion'
    print (uno, dos, tres)

def EXPosicion2(uno, dos='DOS', tres=3):     
    print (uno, dos, tres)

#-----------------------------------------
var_modulo = "valor de var_modulo"
def EXPosicion21(uno, dos=var_modulo, tres=3):
    print (uno, dos, tres)

##def EXPosicion22(uno, dos="DOS", tres=var_funcion):
##    var_funcion = "valor var en funcion"
##    print (uno, dos, tres)
## Da error en el momento de la declaración

def EXPosicion23(uno, dos='DOS', tres=[]):
    elem = str(uno) + str(dos)
    tres.append(elem)
    print (uno, dos, tres)

## En este caso: se van acumulando los valores de los argumentos
##   que se le pasan en subsiguientes llamadas:

def EXPosicion24(uno, dos='DOS', tres=None):
    elem = str(uno) + str(dos)
    if not tres: tres = []
    tres.append(elem)
    print (uno, dos, tres)    
##Modificación de la función, para que no se vayan acumulando los valores
##  en la siguientes llamadas.
#-----------------------------------------
def EXPosicion3(*tupla_parametro): 
    print ('Argumentos recibidos : ' ,tupla_parametro,
           '\nen total: ', len(tupla_parametro),
           '\nde tipo: ', type(tupla_parametro) )
    for argumento in tupla_parametro: 
        print ('\t', argumento)

def EXPosicion4(uno, dos='DOS', tres=3):
    print (uno, dos, tres)   

#Llamadas----------------------------------------------------------------
#Argumentos a parametros por posicion
print ("Argumentos a parametros por posicion")
'''
EXPosicion1 ('UNO', 2, 'Tres')
'''
##Errores:
#a) Menos argumentos que parametros 
#0..N-1 Argumentos --> N Parametros
#-------------------------------------------------------------
#EXPosicion1 ('UNO', 2)        #TypeError: Efuncion1() missing 1 required positional argument: 'tres'
#EXPosicion1 ('UNO', , 'Tres') #invalid syntax (No puede dejar hueco
#EXPosicion1 ('UNO',_, 'Tres') #NameError: name '_' is not defined
'''
EXPosicion1 ('UNO','', 'Tres') 
EXPosicion1 ('UNO',None, 'Tres')
'''

#Solucion1 -->Parametros por omision
#------------------------------------
'''
EXPosicion2 ('1', 3, 'Tres')
EXPosicion2 ('UNO', 2) 
EXPosicion2 ('UNO')   
'''
##Problemas
#Errores:
#1) var_modulo debe existir ANTES de la declaracion de la función
#var_modulo = "var_modulo"
#EXPosicion21('UNO') #NameError: name 'var_modulo' is not defined
'''
EXPosicion21('UNO')
'''
#2) var_funcion No existe en el momento de la declaración de la funcion.
#EXPosicion22('UNOOO') # El error en el momento de "declaración"
#3) Utilizar variables mutables
''' 
EXPosicion23('UNO')
EXPosicion23('DOS')
EXPosicion23('TRES')

#Solucion
EXPosicion24('UNO')
EXPosicion24('DOS')
EXPosicion24('TRES')
'''
#Solucion2 --> Argumentos empaquetados --> Parametros desempaquetando argumentos
#-------------------------------------------------------------------------------
#A)Llamada con argumentos empaquetados en tuplas, listas,..
#Deben mantener el orden 
''''''
arg_tupla = ('el uno',22,333);arg_lista = ['UNO',2,33]  
EXPosicion4(*arg_tupla)
EXPosicion4(*arg_lista)
EXPosicion4('UNO', *(22,333))
EXPosicion4(*['UNO',2],33)

#Ejemplo con funciones nativas --> range()
# llamada normal con argumentos separados
'''
print (list(range(3, 6)))
'''
# llamada con argumentos empaquetados en una lista
'''
argumento = [3, 6,1]
print (list(range(*argumento)))
'''
#B) Llamada con argumentos empaquetados en un diccionario
#Para que funcione debe cumplir reglas parametro fijo-posicional, parametro-Nombre
#Deben mantener el orden
arg_dict ={'uno':'UNO','dos':2,'tres':'tres'}
EXPosicion4(**arg_dict)
EXPosicion4('UNO',**{'dos':2,'tres':'tres'})
#EXPosicion4(**{'uno':'UNO','dos':2},'tres')#Error sintactico
##Positional argument follos keyword argument unpacking

#Solucion3 -->Argumentos y Parametros arbitrarios
#-------------------------------------------------

#################################################################
##Errores:
#b)Más argumentos que parametros
#0..N-1 Argumentos --> 0..N-1 Parametros
#Numero de argumentos desconocido ¿mas?¿menos? que parametros
#---------------------------------------------------------------------- 
#EXPosicion1 ('UNO', 2, 'Tres', 4)
     #TypeError: Efuncion1() takes 3 positional arguments but 4 were given
#Solucion3 -->Argumentos y Parametros arbitrarios
#-------------------------------------------------
'''
EXPosicion3('UNO', 2, 'Tres')
EXPosicion3 ('UNO', 2) 
EXPosicion3('UNO', 2, 'Tres', 4)
'''
'''
tupla1 = ("lunes", "martes", "miercoles","jueves", "viernes")
tupla2 = ("Sabado", "Domingo")
EXPosicion3(tupla1, tupla2)
EXPosicion3(tupla1, ["Sabado", "Domingo"], {1,2,3})
'''
