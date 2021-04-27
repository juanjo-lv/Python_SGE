#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' "Llamadas entre funciones independientes, funciones lambda" '''
#Declaracion de funciones----------------------------------------------

def funcionA1():
    'Funcion sin parametros y solo return'
    return "Hola Mundo"

def funcionA2(nombre, mensaje='Hola'):
    ''' "Funcion con parametros, llamada a otra función  y sin return" '''
    print (mensaje, nombre) 
    print (funcionA1())

def funcionA3(nombre, mensaje='Adios'): print( mensaje, nombre, funcionA1())

var_funcionB = lambda nom, men="Buenas" : funcionA2(mensaje=men, nombre=nom)

#funcion anidada:
def funcionC(): return (lambda a,b:print(a*b))
#funcion anidada 2: sin parametros en la lambda
def funcionD(): return (lambda : print("hola"))

#Pruebas-----------------------------------------------------------------
saludo1 ='Buenos días'; saludo3 ='Buenas noches'
nombre1,nombre2, nombre3 = 'Enrique','Amelia', 'Luisa'
num1,num2 = 4,5
#Llamadas--------------------------------

#llamada a la funcion lambda dentro de una función
funcionC()(num1,num2)
funcionD()()




