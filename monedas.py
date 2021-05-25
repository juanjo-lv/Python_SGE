# Programa que realiza la devolución de una cantidad dada por el usuario en monedas.

# El programa debe cumplir los siguientes requisitos:

# - Solo se disponen de tres tipos de monedas: 5, 2 y 1 €. Crear una lista que contenga estos tres tipos de moneda y usar la lista en la solución.
# - El programa debe preguntar al usuario por una cantidad entera de euros.
# - El programa debe mostrar por pantalla el mínimo número de monedas necesarias para sumar la cantidad introducida por el usuario y cuántas monedas de cada tipo se necesitan para ello. El número de monedas de cada tipo debe guardarse en otra lista.

# Definimnos la lista con los tipos de monedas.
monedas = [5, 2, 1]
# Definimos e inicializamos a cero la lista con el número de monedas de cada tipo.
cambio = [0, 0, 0]
# Pedimos al usuario que introduzca una cantidad entera.
cantidad = int(input("Introduce una cantidad entera de euros: "))
print('Para sumar', cantidad, '€ se necesitan ', end='')
# Recorremos la lista con los tipos de monedas 
for i in range(len(monedas)):
    # Mientras la cantidad a devolver sea mayor que el tipo actual de moneda restamos de la cantidad una moneda de este tipo y añadimos una moneda más a la lista con el cambio de ese tipo de moneda
    while cantidad >= monedas[i]:
        cantidad -= monedas[i]
        cambio[i] += 1
# Mostramos por pantalla el número de monedas necesario que es la suma de las monedas en la lista cambio
print(sum(cambio), 'monedas:')
# Recorremos la lista de tipos de monedas e imprimimos cuántas monedas de cada tipo se necesitan para el cambio.
for i in range(len(monedas)):
    print(cambio[i], 'monedas de ', monedas[i], '€')