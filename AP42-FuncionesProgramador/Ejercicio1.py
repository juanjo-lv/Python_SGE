def repite(caracter,veces):
    cadena = ''
    for i in range(veces):
        cadena = cadena + caracter
    return cadena
resultado = repite('hola',5)
print(resultado)