A = (4,"hola",8,"adios")

def convertir(tup,num1,num2):
    lista = []
    for i in tup:
        if(type(i)==int):
            #es entero
            if(i%num1==0):
                resta = num1-num2
                i = i*resta
                lista.append(i)
        else:
            #es string
            i+= f"({str(len(i))})"
            lista.append(i)
         
    return lista

print(convertir(A,2,3))
