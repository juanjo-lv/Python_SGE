
x = input("teclea los numeros, separados por comas")

tup = x.replace(",","")
tupla = tuple(tup)

print("la tupla es",tupla)

lista = []

for elem in tupla:
    lista.append(int(elem))


lista = [elem for elem in tupla]
print(lista)

# print("la lista es :",lista)
