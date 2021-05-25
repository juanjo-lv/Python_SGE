def factorial(numero):
    cad = f"{numero}! = "
    cont = 1
    for i in range(1,numero+1,1):
        cont*=i
        if(i==numero):
            cad+=f"{i} = "
        else:
            cad+=f"{i} x "
                
    cad+=f"{cont}" 
    return cad

print(factorial(4))
