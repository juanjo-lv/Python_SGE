dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
dias_semana_dic = {}
print('--- normal ---')
for i in range(len(dias_semana)):
    dias_semana_dic[i+1] = dias_semana[i]

print(dias_semana_dic)
print('--- comprehension ---')

dias_semana_dic.clear()

dias_semana_dic = {i+1:dias_semana[i] for i in range(len(dias_semana))}

print(dias_semana_dic)