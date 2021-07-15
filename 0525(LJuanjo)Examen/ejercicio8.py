'''
Programa que tiene un menu y que nos da a elegir 3 opciones
    1- ejecutar una funcion al que le pasamos palabras separadas por espacio y crea un diccionario contando cuantas veces se repite
    2- ejecutar una funcion que llama a la primera funcion y devuelve una tupla con el valor más repetido y las veces que se repite
    3- ejecutar una función que al pasarle una cantidad y te lo devuelve en monedas de valor 5, 2 y 1 

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
    monedas = [2, 1, 0.5]
    cambio = [0, 0, 0]
    cantidad = float(input("Introduce una cantidad entera de euros: "))
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
    



