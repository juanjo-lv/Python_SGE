dic = {1:'uno',45:'dos',34:'tres',4:'cuatro'}
lista = [1,2,3,4]

dic2 = {clave:valor for clave,valor in dic.items() if clave not in lista}
print(dic2)