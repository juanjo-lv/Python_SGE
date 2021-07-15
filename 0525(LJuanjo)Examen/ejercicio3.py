def miFuncion(*num):
    ''' docstring de miFuncion'''
    total = 0
    media = 0
    for n in num:
        total+=n   
    media = total/len(num) 
    lista = [total,media]
    return lista   

tupla=(1,2,3,4)
lista=["A","B","C"]
dic = {1:"A",2:"B",3:"C"}

