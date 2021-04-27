#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' Funciones de orden superior '''

#Declaracion de Funciones--------------------------------------------------
def funcion(nombre="ElMio"): return "Hola " + nombre

def funcionSuperior(funcion=None): 
    'Se recibe una funcion y retorna llamando a otra funcion'
    tunombre = input ("Teclea tu nombre: ")
    return funcion(tunombre)
    
#Pruebas------------------------------------------------------------------
resultado = funcionSuperior(funcion)
print (resultado)
