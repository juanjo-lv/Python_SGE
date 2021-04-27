#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' "Anidamiento  de funciones "independientes" '''

#Declaracion de funciones----------------------------------------------
def funcionA1():
    'Funcion sin parametros y solo return'
    return "Hola Mundo"

def funcionNido_Ind():
    #Declaracion de las funciones anidadas------------------------- --
    def funcionA2(nombre, mensaje='Hola'):
        '''Funcion con parametros, llamada a otra función  y sin return'''
        print (mensaje, nombre) 
        print (funcionA1())

    def funcionA3(nombre, mensaje='Adios'): print( mensaje, nombre, funcionA1())

    var_funcionB  = lambda nom, men="Buenas" : funcionA2(mensaje=men, nombre=nom)

    def funcionC(): return (lambda a, b : print (a * b))

    #Comprobar existencia según ambitos------------------------------------

    #Fin comprobaciones-------------------------------------------------------

    #Codigo propio de la funcionNido_Ind()----------------------------------
    saludo1 ='Buenos días'; saludo3 ='Buenas noches'
    nombre1,nombre2, nombre3 = 'Enrique','Amelia', 'Luisa'
    #Llamadas entre funciones del "nido" : funcionNido_Ind() 
    funcionA2(saludo1,nombre1 )
    print()
    funcionA3(nombre2)
    print()
    var_funcionB(men=saludo3, nom=nombre3)

#Pruebas-----------------------------------------------------------------------
#Comprobar existencia según ambitos------------------------------------------

#Fin comprobaciones

#Llamadas ---------------------------------------------------------------------
funcionNido_Ind()         




