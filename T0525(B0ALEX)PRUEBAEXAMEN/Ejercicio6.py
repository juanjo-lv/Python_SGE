import Ejercicio5 as ej5

while():
    multiplo = int(input("Introduce el multiplo: "))
    elem = int(input("Introduce el numero de elementos: "))
    generad =  ej5.genMultiplos(multiplo=multiplo, elem=elem)
    lista = [i for i in generad]
    print(lista)
    seguir = input("Quieres seguir? (si/no): ")
    if(seguir == "no"):
        break