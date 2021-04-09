
def esUnNumero():
    numero = input("Introduce un numero")
    try:
        numero = int(numero)
        if numero > 0:
            print("Tu numero es entero positivo")
        elif numero < 0:
            print("Tu numero es entero negativo")
    except:    
        if ('0o'in numero) or ('0O' in numero):
            try:
                oct = int(numero,8)
                if oct < 0:
                    print("Tu numero es octal y negativo")
                elif oct>0:
                    print("Tu numero es octal y positivo")
            except:
                print("El numero elegido no está en base 8")
        elif ('0x' in numero or 'OX' in numero):
            try:
                hex = int(numero,16)
                if hex < 0:
                    print("Tu numero es hexadecimal y negativo")
                elif hex > 0:
                    print("Tu numero es hexadecimal y positivo")
            except:
                print("El numero elegido no está en base 16")
        elif ('0b' in numero) or ('0B' in numero):
            try:
                bin = int(numero,2)
                if bin < 2:
                    print("Tu numero es binario y negativo")      
                elif bin>2:
                    print("Tu numero es binario y positivo")
            except:
                print("El numero elegido no está en base 2")            
esUnNumero()