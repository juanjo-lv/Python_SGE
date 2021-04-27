#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Ejemplos de funciones dinamicas/ llamadas de retorno '''

#Declaración funciones módulo -------------------------
def funcion(nombre="ElMio"): 
    return "Hola " + nombre

#Pruebas------------------------------------------------------------------
salir = "No"        
while (salir != "S"):
    #---------------------------------------------------------------------
    nombrefun = str(input('Teclea: funcion, salir, o lo que quieras ') )
    #1. Comprobar su existencia en ámbitos: local y global
    '''
    print ("En ambito local ", nombrefun in locals())
    print ("Local\n", dir())
    print ("En ambito global ", nombrefun in globals())
    print ("Global\n", dir())
    '''
    #2. Comprobar si existe en ambito local, y si es una función e invocable
    #   "directamente", sin utilizar "variables auxiliares"
    if nombrefun in locals():
        print('El nombre ', nombrefun, ' Existe en el ambito local' )
        #2.0. Comprobar si es un objeto función
        print (' Existe nombrefun ', type(nombrefun),
               ' y es : ', type(locals()[nombrefun])  )
        #2.1. Comprobar (sea o no función) si es invocable
        if callable(locals()[nombrefun]): 
            print (' La función ', nombrefun, ' se puede llamar ')
            #Siguiente paso: Utilizar la función según necesidad
            #Llamada a la función. Sin argumentos
            print(locals()[nombrefun]() )
        else :
            print (' La función ', nombrefun, ' NO se puede llamar ')            
    else :
        print('El nombre ', nombrefun, ' no existe en el ambito local' )
        
    #3. Comprobar si existe en ambito global, y si es una función e invocable
    #   utilizando una "varible auxiliar"            
    if nombrefun in globals():
        print('El nombre ', nombrefun, ' Existe en el ambito global' )        
        var_funcion = globals()[nombrefun]        
        print (' Existe nombrefun ', type(nombrefun),
               ' y es : ', type(var_funcion) )
        #3.1. Comprobar (sea o no función) si es invocable
        if callable(var_funcion):
            print (' La función ', nombrefun, ' se puede llamar ')
            #Siguiente paso: Utilizar la función según necesidad
            #Llamada a la función. Con argumentos
            tunombre = input ("Teclea tu nombre: ")
            #tunombre = "Eltuyo"
            print(var_funcion(tunombre))
        else :
            print (' La función ', nombrefun, ' NO se puede llamar ')            
    else :
        print('El nombre ', nombrefun, ' no existe en el ambito global' )

    #---------------------------------------------------------------------    
    salir = input("Pulsa S para salir ")    
else:
   pass
