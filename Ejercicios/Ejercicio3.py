

def convertir():
    numero = int(input("Introduce el numero que quieres convertir"))
    '''
    [x:] --> elimina los 2 primero numeros, es decir el prefijo
    zfill(n) --> representa el numero en n digitos
    '''
    print(f"El numero es {numero}")
    print(f"en base 2 es: {bin(numero)[2:].zfill(4)}")
    print(f"en base 8 es: {oct(numero)[2:].zfill(4)}")
    print(f"en base 16 es: {hex(numero)[2:].zfill(4)}")

convertir()