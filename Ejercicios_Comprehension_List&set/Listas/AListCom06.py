import math
lista = [4,6,4,12,7]

#facto(n) = n*m-1*n-2...*..*n-m*1
facto = [math.factorial(elemento) for elemento in lista]
print(facto)
