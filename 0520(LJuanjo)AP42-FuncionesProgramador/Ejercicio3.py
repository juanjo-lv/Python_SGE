
def opera(operacion='suma',*numeros):    
    resultado = 0
    if(operacion == 'suma'):
        for i in numeros:
            if(numeros.index(i)==0):
                resultado = i
            else:
                 resultado += i 
    elif(operacion == 'resta'):
        for i in numeros:
            if(numeros.index(i)==0):
                resultado = i
            else:
                resultado = resultado - i          
    elif(operacion == 'producto'):
        for i in numeros:
            if(numeros.index(i)==0):
                resultado = i    
            else:
                 resultado = resultado * i    
    elif(operacion == 'division'):
        for i in numeros:
            if(numeros.index(i)==0):
                resultado = i   
            else:
                resultado = resultado / i
    elif(int(operacion)):
        resultado = operacion
        for i in numeros:
            resultado += i
        
    return resultado

             
print(opera('resta',5,4,2))
print(opera('producto',2,3,4,5,6))
print(opera('division',4,8,2))
print(opera(4,5,3))    
