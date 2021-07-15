dic = {"hola":"hello","adios":"bye","perro":"dog"}

def traducir(palabra):
    if palabra in dic.keys():
        print(dic[palabra])
    else:
        print("la palabra no se encuentra en el diccionario")    

print(traducir("gato"))


