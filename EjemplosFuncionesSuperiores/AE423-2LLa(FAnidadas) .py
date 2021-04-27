#! /usr/bin/env python
# -*- coding: utf-8 -*-
''' "Anidamiento  de funciones "independientes" '''
#Declaracion de funciones
#----------------------------------------------------- 
def funcionA1(): return "Hola Mundo"

def funcionA2(nombre, mensaje='Hola'):
        '''Funcion con parametros, llamada a otra función  y sin return'''
        print (mensaje, nombre) 
        print (funcionA1())
        
def funcionNido(nom_fun=""):
#    print ("En funcion: ", funcionNido.__name__)
    #Declaracion de las funciones anidadas---------------------------
    def enNido_1():
        print ("En funcion: ", enNido_1.__name__)
    def enNido_2(nombre="Xomision"):
         print ("En funcion: ", enNido_2.__name__)
         print ("Hola ", nombre)
    def enNido_3(nomfun2=None):
         print ("En funcion: ", enNido_3.__name__)        
         #Declaracion de las funciones anidadas----------------
         def enNido_31():
             print ("En funcion: ", enNido_31.__name__)
         def enNido_32(num1=0, num2=0):
             print ("En funcion: ", enNido_32.__name__)
             print ("La suma de ", num1, " + ", num2, " es: ", (num1 + num2)) 
         #Codigo -----------------------------------------------------
         anidadas = {'enNido_31':enNido_31,'enNido_32':enNido_32}
         if (nomfun2 == None) or (nomfun2 not in anidadas):  pass
         else: return anidadas[nomfun2] #Sin parentesiso con parentesis  

    var_funcionB  = lambda nom, men="Buenas" : funcionA2(mensaje=men, nombre=nom)         
    def funcionC(): return (lambda a, b : print (a * b))

    #Codigo propio de la funcionNido_Ind()----------------------------------
    fun_locales = {'enNido_1': enNido_1,'enNido_2': enNido_2,'enNido_3': enNido_3,
                  'funcionC':funcionC,'var_funcionB':var_funcionB}
    if nom_fun in fun_locales: fun_a_llamar = fun_locales[nom_fun]

    #Llamadas--------------------- 
    return fun_a_llamar   

#Pruebas-----------------------------------------------------------------------
nombre ="Luisa"
nom_funcion = 'enNido_1'
#Llamadas ---------------------------------------------------------------------
funcionNido('enNido_1')()
print("--------------------")
funcionNido('enNido_2')(nombre)
print("--------------------")
funcionNido('enNido_3')()
print("--------------------")
funcionNido('funcionC')()(4,5)
print("--------------------")
funcionNido('var_funcionB')(nombre,"hola")
print("--------------------")
print("--------------------")
print("--------------------")

funcionNido('enNido_3')('enNido_31')
funcionNido('enNido_3')('enNido_31')()
funcionNido('enNido_3')('enNido_31')(4,5)

