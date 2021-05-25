cadena = input('teclea los numeros, separador por comas: ')
numeros_separados = tuple(cadena.split(','))
print(f'La tupla es {numeros_separados}')

lista = []
for i in numeros_separados:
    lista.append(i)

print(f'La lista es {lista}')