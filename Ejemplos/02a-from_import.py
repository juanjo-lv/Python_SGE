#! /usr/bin/env python
#-*- coding: utf-8 *-*
'''
Importando con from import los modulos: platform y math
y con import el modulo os
'''
from platform import __doc__, system
from math import pi
import os

#Utilización----------------------------------------
print ("Tiene como docuemntación   " + __doc__)
print ("El sistema operativo es " + system())
print ("La constante PI tiene el valor " , pi) 

print('----------------------------------------------')
input("Pulsa cualquier tecla para limpiar pantalla")
os.system("cls")

#Esperar pulsacion para salir
input("Pulsa cualquier tecla para terminar") 
