#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''Caracteristicas funciones'''
#-----------------------------------------
def caracteristicasFunc(objeto, mas=None):
    '''Caracteristicas de una función'''
    print ('\nLa Funcion : ', objeto.__name__ ,
           '\n docstring: ', objeto.__doc__)
    print (" tipo ", type(objeto), " \n id: ", id(objeto) )
    print ('* Contenido:>> ', objeto )
    if '__dict__'  in dir(objeto):
          print ('* Nombres:>>  ')
          nombres = objeto.__dict__
          print (nombres)
          for elem in nombres:
               print ('\t', elem, ' : ', nombres[elem])
    if '__module__'  in dir(objeto):
          print ('* Modulo:>> ', objeto.__module__ )
    if mas != None:
        print ('Listado de propiedaded y métodos \n')
        lista_dir = dir(objeto)
        print (lista_dir)


