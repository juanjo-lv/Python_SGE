#Importando
from mholadios import saludo, alumno1, dias_semana

#Utilización----------------------------
#---------------------------------------
#Nota: Se ejecutan las instrucciones que existan en los ficheros importados
print ("Empezamos el codigo de nuestro fichero")


#print (saludo(alumno1["Nombre"]) + " hoy es " + dias_semana[0]) #Error

#print (saludo(alumno1["Nombre"]) + " hoy es ",  dias_semana[0]) #Error

print (saludo(alumno1["Nombre"]) , " hoy es ",  dias_semana[0]) #Se incluye respuesta función

input("Pulsa cualquier tecla para terminar") #Esperar pulsacion para salir
