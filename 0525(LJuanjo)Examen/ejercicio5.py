from ejercicio1 import *
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *
from ejercicio5 import *
from ejercicio6 import *
from ejercicio7 import *
import os

def formulario():
    salir = False
    while not salir:
        respuesta = str(input("Introduce una opcion: \n 1) E1 \n 2) E2 \n 3) E3 \n 4) E4 \n 6) E6 \n 7) E7")).tolower()
        if(respuesta=="1"):
            os.system('python ejercicio1.py')
        elif(respuesta=="2"):
            os.system('python ejercicio2.py')
        elif(respuesta=="3"):
            os.system('python ejercicio3.py')
        elif(respuesta=="4"):
            os.system('python ejercicio4.py')   
        elif(respuesta=="6"):
            os.system('python ejercicio6.py')
        elif(respuesta=="7"):
            os.system('python ejercicio7.py')
        elif(respuesta=="s"):
            salir = True    
        else:
            print("la opcion no es válida")
formulario() 
    