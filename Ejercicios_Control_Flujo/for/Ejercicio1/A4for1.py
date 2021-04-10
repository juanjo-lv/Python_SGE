lista = ['gato','perro','canario','peces']

def analizoLista(lista):
    print("la lista contiene ",len(lista)," elementos")
    for i in range(len(lista)):
        print("pos: ",i," -> ",lista[i]," con ", len(lista[i])," carácteres")

analizoLista(lista)