import math

#a) algunas funciones de math

'''
    math.ceil(x) --> Devuelve el entero mas proximo mayor o igual a x
    math.floor(x) -->  Devuelve el entero mas proximo menor o igual a x
    math.gcd(a,b) --> Devuelve el maximo común divisor de a y b
    math.isnan(x) --> Devuelve True si es un num y si no False
    math.sin(x)/math.cos(x)/math.tan(x) --> Devuelve seno coseno y tangente de x
 
'''



lista = [4,6,4,12,7]

#facto(n) = n*m-1*n-2...*..*n-m*1
facto = [math.factorial(elemento) for elemento in lista]
print(facto)

