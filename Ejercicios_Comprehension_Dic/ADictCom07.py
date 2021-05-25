# dic = {'hola':'mundo','limon':'amarillo','perro':'grande'}
# dic2 = {clave: valor for valor, clave in dic.items()}
# print(dic2)

dic ={"hola":"mundo","limon":"amarillo","perro":"kaje"}

dic2 = {1:2,3:4,5:6}

#dic3 tiene la clave de dic2 y el valor de dic

dic3 = dict(zip(dic2,dic))

print(dic3)

