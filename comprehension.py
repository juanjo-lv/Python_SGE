

def ejemplo3():
    #Crear una lista a partir de los elementos comunes de dos listas, una con multuiplos de 4 y otra con los multiplos de 5, que estén 
    #comprendidos  entre -20 y50
    listaA = [elem for elem in range(primero,ultimo) if elem % multiplo1 == 0]
    listaB = [elem for elem in range(primero,ultimo) if elem % multiplo2 == 0]

    listaC = [elem for elem in range(primero,ultimo,paso) if (elem in listaA) and (elem in listaB)]

def ejemplo4():
    #Visualizar una lista con las letras consonantes, de una cadea dada, en mayusculas
    print([letra.upper() for letra in cadena if letra.lower() not in vocales])

def ejemplo4b():
    #a partir de una lista numérica dada, Visualiza una lista con todos los elementos covertidos a números en octal
    lista_dada = [1,2,3,4]; print ('lista_dada\n',lista_dada)
    lista_octal = [oct(elem) for elem in range(0,len(lista_dada))]
    print(lista_octal)

