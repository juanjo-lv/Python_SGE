lista = ["perro","gato",32,True,"Pez"]

#tradicional
print("Bucle tradicional: ")
print()
for i,elemento in enumerate(lista):
    print(i,elemento)
print()


#con comprension:
print("Bucle comprehension: ")
print()
dic = {i:elemento for i,elemento in enumerate(lista)}
print(dic)