diccionario = {'Juan':111, 'Antonio':222, 'Pedro':333}
tupla = ('Luis', 5, 'sol', 'luna')

def zip(diccionario, tupla):
    key_list = list(diccionario.keys())
    val_list = list(diccionario.values())
    for i in range(0, 3):
        print(f'De la tupla es: {tupla[i]} y del Diccionario es: {key_list[i]} con valor {val_list[i]}')
        

zip(diccionario, tupla)