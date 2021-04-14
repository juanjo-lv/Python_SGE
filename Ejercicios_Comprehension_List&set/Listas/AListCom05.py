lista1 = [1,2,3];lista2=[4,5,6];lista3=[7,8,9]

lista4 = []
#solucion de multiplicar uno con todos sin repetición
#[lista4.append(v1*v2*v3) for v1 in lista1 for v2 in lista2 for v3 in lista3 if(v1*v2*v3) not in lista4]

#Solucion de multiplicar cada posiciones de las listas entres si
lista4 = [lista1[elemento]*lista2[elemento]*lista3[elemento] for elemento in range(0,3)]

print(lista4)