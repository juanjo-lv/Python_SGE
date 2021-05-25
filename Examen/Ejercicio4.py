import keyword
# print(keyword.kwlist)

respuesta = input("Ejercicio cuatro \n ****** \n A) Comprobar palabras reservadas \n B) Comprobar funciones integradas \n C) Comprobar nombres del ambito \n S) Salir \n Seleciona una opcion:").lower()
numero = 2
booleano = False

while(respuesta!='s'):

    if(respuesta=='a'):
        reservada = str(input("introduce un palabra reservada"))
        if reservada in keyword.kwlist:
            print("es reservada")
        else:
            print("no es reservada")            
       
    elif(respuesta=='b'):
       print("sin hacer")
      
    elif(respuesta == 'c'):
        nombre = str(input("Introduce nombre:"))
        if(nombre in globals() or nombre in locals()):
            print(" Está en el módulo"," tipo: ",type(nombre))
        else:
            print("No existe")
       
    
    respuesta = input("Ejercicio cuatro \n ****** \n A) Comprobar palabras reservadas \n B) Comprobar funciones integradas \n C) Comprobar nombres del ambito \n S) Salir \n Seleciona una opcion:")