'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene 
y su frecuencia. 
Escribir otra función que reciba el diccionario generado con la función anterior y 
devuelva una tupla con la palabra más repetida y su frecuencia.

'''
def contar_palabras(texto):
    texto = texto.split()
    palabras = {}
    
    #comprehension
    #palabras = {i:palabras[i]+1 if palabras[i]>1 else 1 for i in texto}

#forma sin comprimir
    for i in texto:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def repetidas(palabras):
    num_palabra = ''
    freq_palabra = 0
    for palabra, freq in palabras.items():
        if freq > freq_palabra:
            num_palabra = palabra
            freq_palabra = freq
    return num_palabra, freq_palabra

texto = str(input("Escribe el texto que quieres comprobar"))
print(contar_palabras(texto))
print(repetidas(contar_palabras(texto)))