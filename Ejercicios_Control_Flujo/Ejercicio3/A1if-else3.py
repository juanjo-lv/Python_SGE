numero = int(input("elige un numero"))

if 0 < numero < 100 :
    print("tu numero está entre el 0 y el 100")
elif numero > 100 and (numero%2 ==0):
    print("Tu numero es mayor a 100 y par")
elif numero < 100 and (numero%2!=0):
    print("Tu numero es menor a 100 e impar")