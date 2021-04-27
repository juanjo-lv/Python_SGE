#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' Argumentos a Parametros por nombre '''

def EXNombre1(nombre, apellido, mensaje): 
    print (mensaje, nombre, apellido)

def EXNombre2(nombre='Luis', apellido='Sanchez', mensaje='Hola'): 
    print (mensaje, nombre, apellido)
    
#-----------------------------------------
var_modulo = "valor de var_modulo"
def EXNombre21(nombre, apellido=var_modulo, mensaje='Hola'):
    print (mensaje, nombre, apellido)

##def EXNombre22(nombre,apellido=var_funcion, mensaje='Hola'):
##    var_funcion = "valor var en funcion"
##    print (mensaje, nombre, apellido)
### Da error en el momento de la declaración

def EXNombre23(nombre='Luis', apellido='Sanchez', mensaje=[]):
    elem = str(nombre) + str(apellido)
    mensaje.append(elem)
    print (mensaje, nombre, apellido)
## En este caso: se van acumulando los valores de los argumentos
##   que se le pasan en subsiguientes llamadas:

def EXNombre24(nombre='Luis', apellido='Sanchez', mensaje=None):
    elem = str(nombre) + str(apellido)
    if not mensaje: mensaje = []
    mensaje.append(elem)
    print (mensaje, nombre, apellido) 
##Modificación de la función, para que no se vayan acumulando los valores
##  en la siguientes llamadas.
#-----------------------------------------
def EXNombre3(**dict_parametro): 
    print ('Argumentos recibidos : ' ,dict_parametro,
           '\nen total: ', len(dict_parametro),
           '\nde tipo: ',  type(dict_parametro) )
    for argumento in dict_parametro:
        print ('\tLa clave: ', argumento ,
              ' tiene como valor: ', dict_parametro[argumento])

def EXNombre4(nombre='Luis', apellido='Sanchez', mensaje='Hola'):
    print (mensaje, nombre, apellido)  
#Llamadas----------------------------- 
#Argumentos a parametros por nombre
print ("Argumentos a parametros por nombre")
'''
EXNombre1(mensaje="Buen día", nombre="Juancho",apellido ="Ruiz" ) 
'''
##Errores:
#a) Menos argumentos que parametros 
#0..N-1 Argumentos --> N Parametros
#-------------------------------------------------------------
#EXNombre1(nombre="Juancho",apellido ="Ruiz" )  #>> TypeError: saludar() missing 1 required positional argument: 'mensaje'
#EXNombre1(mensaje="Buen día",nombre="Juancho") #>> TypeError: saludar() missing 1 required positional

#Solucion1 -->Parametros por omision
#------------------------------------
''' 
EXNombre2(mensaje="Buen día", nombre="Juancho",apellido ="Ruiz" ) 
EXNombre2(nombre="Juancho",apellido ="Ruiz" )
EXNombre2(apellido ="Martinez" )
'''
##Problemas
#Errores:
#1) var_modulo debe existir ANTES de la declaracion de la función
#var_modulo = "var_modulo"
#EXNombre21(nombre="Juancho") #NameError: name 'var_modulo' is not defined
'''
EXNombre21(nombre="Juancho")
'''
#2) var_funcion No existe en el momento de la declaración de la funcion.
#EXNombre22(nombre="Juancho") # El error en el momento de "declaración"
#3) Utilizar variables mutables
''' 
EXNombre23(apellido='Uceta')
EXNombre23(apellido='Giron',nombre='Maria' )
EXNombre23(nombre='Luisa')

#Solucion
EXNombre24(apellido='Uceta')
EXNombre24(apellido='Giron',nombre='Maria' )
EXNombre24(nombre='Luisa')
'''
#Solucion2 --> Argumentos empaquetados --> Parametros desempaquetando argumentos
#-------------------------------------------------------------------------------
#A)Llamada con argumentos empaquetados en tuplas, listas,..
#Para que funcione debe cumplir reglas parametro fijo-posicional, parametro-Nombre
#Mantener orden
''' '''
arg_tupla = ('Luis','Sanchez', 'Adios')
arg_lista=['Luis','Sanchez', 'Hasta la vista']
EXNombre4(*arg_tupla)
EXNombre4(*arg_lista)
#EXNombre4(nombre='Luis', *('Sanchez', 'Adios'))
##TypeError: EXNombre4() got multiple values for argument 'nombre'
#EXNombre4( *('Sanchez', 'Adios'),nombre='Luis')
##TypeError: EXNombre4() got multiple values for argument 'nombre'

#B) Llamada con argumentos empaquetados en un diccionario
''' 
arg_dict ={'mensaje':"Buen día",'nombre':"Juancho",'apellido':"Ruiz"}
EXNombre4(**arg_dict)
EXNombre4(mensaje="Buen día",**{'apellido':"Ruiz",'nombre':"Juancho"})
EXNombre4(apellido="Ruiz",**{'mensaje':"Buen día",'nombre':"Juancho"})
'''
#Solucion3 -->Argumentos y Parametros arbitrarios
#-------------------------------------------------
###############################################################
##Errores:
#b) Más argumentos que parametros
#0..N-1 Argumentos --> 0..N-1 Parametros
#Numero de argumentos desconocido ¿mas?¿menos? que parametros
#---------------------------------------------------------------------- 
#EXNombre1(mensaje="Buen día", nombre="Juancho",apellido ="Ruiz", edad=35 ) 
#TypeError: saludar1() got an unexpected keyword argument 'edad'
#Solucion3 -->Argumentos y Parametros arbitrarios
#-------------------------------------------------       
'''
EXNombre3(mensaje="Buen día", nombre="Juancho",apellido ="Ruiz" ) 
EXNombre3(nombre="Juancho",apellido ="Ruiz")
EXNombre3(edad=35, mensaje="Buen día", nombre="Juancho",apellido ="Ruiz" )
'''
           


