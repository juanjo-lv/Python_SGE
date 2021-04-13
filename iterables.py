def func_generadora_numFin(inicio=0, numero=10):
    #genera una secuencia infinita
    fin = inicio + numero
    while inicio < fin:
        yield inicio,fin
        inicio +=1
    
func_generadora_numFin()