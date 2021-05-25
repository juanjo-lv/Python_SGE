def generaMultiplos(multiplo=2, empieza=1, elementos=None):
    for empieza in range(empieza, elementos+1, 1):
        if(empieza%multiplo == 0):
            #yield para generar
            yield empieza

numeros = generaMultiplos(multiplo=5, elementos=100)


lista =[i for i in numeros]

tupla = tuple(lista)

