#! /usr/bin/env python
#-*- coding: utf-8 *-* 
"""
Ejemplos:
 Contenido de un módulo
 Ámbito de las variables
 Tipos de variables
"""

#Funciones  
#----------------------------
def saludo(nombre):
  print("Hola, " + nombre)

def despedida(nombre):
  print("Adios, " + nombre)
  return nombre

#Variables
#----------------------------
nombre = ""
dias_semana = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
alumno1 = { "Nombre" : "Maria",  "Apellido1" : "Sanchez", "Modulo": "SGE", "Nota" : 10 } 

#Utilización----------------------------
#---------------------------------------

saludo('Rosa')
print(nombre)
despedida('Rosa')
print(nombre)
nombre = despedida('Luis')
print(nombre)
nombre = input("Escribe tu nombre: " )
saludo(nombre)
##
print ("El primer día de la semana es el " + dias_semana[0])
print ("El día de mañana, es el ayer de pasado mañana") 

print ("El nombre del alumno es " + alumno1["Nombre"])
campo="Apellido1"
print ("y su apellido " + alumno1[campo])


