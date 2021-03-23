#Importando
#Nota el nombre del modulo y el alias no pueden utilizarse a la vez
#---------------------------------------
import holadios as ha   # la dirección debe ser relativa  o absoluta
#import holadios

#Utilización----------------------------
#---------------------------------------
#Nota: Se ejecutan las instrucciones que existan en los ficheros importados
#Con este formato es necesario anteponer el nombre o el alias
print ("--------------------------------------------------")
print ("Empezamos el codigo de nuestro fichero")
print ("--------------------------------------------------")
print ("Tiene como docuemntación   " + ha.__doc__)
print ("El nombre del modulo es: " + ha.__name__)
"""
holadios.saludo('Rosa')
print(holadios.nombre)
holadios.despedida('Rosa')
"""
ha.saludo('Rosa')
print(ha.nombre)
ha.despedida('Rosa')
#
print(ha.nombre)
nombre = ha.despedida('Luis')
print(ha.nombre)
#
input("Pulsa cualquier tecla para terminar") 
