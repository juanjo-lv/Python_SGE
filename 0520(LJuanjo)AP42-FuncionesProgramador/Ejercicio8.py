lista = [(3,5),(4,5),(6,7)]

area = lambda lista: [('Area : ',(x[0]*x[1])/2 , 'Base: ',x[0],'Altura: ',x[1]) for x in lista]

for i in area(lista):
    for e in i:
        print(e)
    print()

