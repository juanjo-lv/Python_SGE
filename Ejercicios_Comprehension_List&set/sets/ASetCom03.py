import math
lista = [12,"hola",23,"heyyyy",12,"sol",7]
n = 3;

myset = {elemento*2 if isinstance(elemento,str) else math.pow(n,elemento) for elemento in lista}
print(myset)