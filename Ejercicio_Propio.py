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

def devolvermonedas():
    monedas = [5, 2, 1]
    cambio = [0, 0, 0]
    
    cantidad = int(input("Introduce una cantidad entera de euros: "))
    print('Para sumar', cantidad, '€ se necesitan ', end='')
    for i in range(len(monedas)):   
        while cantidad >= monedas[i]:
            cantidad -= monedas[i]
            cambio[i] += 1   
    print(sum(cambio), 'monedas:')  
    for i in range(len(monedas)):
        print(cambio[i], 'monedas de ', monedas[i], '€')

#Ejecución del programa

salir = False
while not salir:
    respuesta = input("Elige una opción : \n 1) contar palabras \n 2) contar palabras repetidas \n 3) contar monedas \n 4) salir \n")
    
    if(respuesta=="1"):
        texto = str(input("Escribe el texto que quieres comprobar"))
        print(contar_palabras(texto))
    elif(respuesta=="2"):
        texto = str(input("Escribe el texto que quieres comprobar"))  
        print(repetidas(contar_palabras(texto))) 
    elif(respuesta=="3"):
        devolvermonedas()
    elif(respuesta=="4"):
        salir = True 
print("Adiós")    
    



