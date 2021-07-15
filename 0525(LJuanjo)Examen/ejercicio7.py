def generamultiplicaciones(num1, num2,numParar):
    empieza = num1
    for empieza in range(1,numParar,1):
         empieza *= num2
         yield empieza

gen = generamultiplicaciones(2,2,7)


lista = [i for i in gen]
print(lista)