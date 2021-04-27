#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' Llamadas dinamicas / llamadas de retorno '''

#Declaracion de Funciones--------------------------------------------------
def funcion(nombre="ElMio"): 
    return "Hola " + nombre
def funcionSuperior(funcion=None): 
    'Se recibe una funcion y retorna llamando a otra funcion'
    tunombre = input ("Teclea tu nombre: ")
    return funcion(tunombre)
    
#Pruebas------------------------------------------------------------------
salir = "No"        
while (salir != "S"):
    #---------------------------------------------------------------------
    nombrefun = str(input('Teclea: funcion, salir, o lo que quieras ' ))


    #---------------------------------------------------------------------    
    salir = input("Pulsa S para salir ")    
else:
   pass
