lista1 = [1,2,3];lista2=[4,5,6];lista3=[7,8,9]

# lista4 = [v1*v2*v3 for v1 in lista1 for v2 in lista2 for v3 in lista3]

#revisar ejercicio
lista4 = [lista1[elemento]*lista2[elemento]*lista3[elemento] for elemento in range(0,3)]

print(lista4)