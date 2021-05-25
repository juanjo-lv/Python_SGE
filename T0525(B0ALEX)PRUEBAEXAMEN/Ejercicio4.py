import keyword
import builtins


def palabraReservada():
    print('')

    palabra = input('Indique palabra reservada a comprobar: ')

    if(palabra in keyword.kwlist):
        print(f'\nLa palabra "{palabra}" existe como palabra reservada')
    else:
        print(f'\nLa palabra "{palabra}" no existe como palabra reservada')
    print('')


def funcionIntegrada():
    print('')

    funcion = input('Indique funcion integrada a comprobar: ')

    if(funcion in dir(builtins)):
        print(f'\nLa funcion "{funcion}" existe como funcion integrada')
    else:
        print(f'\nLa funcion "{funcion}" no existe como funcion integrada')
    print('')


def menu():
    while(True):
        print('Ejercicio cuatro')
        print('*****************')
        print('a) comprobar palabra reservada')
        print('b) comprobar funciones integradas')
        print('c) comprobar nombres del ambito')
        print('s) salir')
        opcion = input('Selecciona opcion: ')
        if(opcion == 'a'):
            palabraReservada()
            pass
        elif(opcion == 'b'):
            funcionIntegrada()
            pass
        elif(opcion == 'c'):
            pass #esta no la he entendido
        elif(opcion == 's'):
            break
        print('')



menu()