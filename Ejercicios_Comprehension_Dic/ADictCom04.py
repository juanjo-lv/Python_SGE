tupla = (1,2,3,4,5)
lista = ['uno','dos','tres','cuatro','cinco']

dic = {elemento:elemento2 for elemento2 in lista for elemento in tupla}
print(dic)

