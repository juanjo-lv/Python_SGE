import Ejercicio5

respuesta = ""

while respuesta!="*":
    mul = int(input("introduce el multiplo"))
    elem = int(input("introduce el numero de elementos"))
    gen = Ejercicio5.generaMultiplos(multiplo=mul , elementos = elem)
    
    lista = [i for i in gen]
    tupla = tuple(lista)

    print(lista)
    print(tupla)

    respuesta = str(input("Sigues?"))
    if(respuesta=="*"):
        print("Finalizado")



