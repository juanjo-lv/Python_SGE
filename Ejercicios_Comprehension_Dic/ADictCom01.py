numeros = [1,2,3,4,5]
dic = {str(elemento):elemento for elemento in numeros }
print(dic)


numeros2 = [1,2,2,3]
dic2 = {str(elemento):elemento for elemento in numeros2}
print(dic2)
print("se pierde información al repetirse un numero")



dic2 = {str(elemento):numeros2[elemento] for elemento in range(len(numeros2))}
print(dic2)
print("Esto es una posible solución")
