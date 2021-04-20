#dir(builtings)

def funcionesPython():
    cont = 0
    while cont < len(dir(__builtins__)):
        print(f"Numero: {cont+1} metodo/propiedad : {dir(__builtins__)[cont]}")
        cont+=1

funcionesPython()
