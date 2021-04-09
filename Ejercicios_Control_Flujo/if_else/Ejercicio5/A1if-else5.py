num1, num2, num3 = 4,3,5

if (num1>num2):
    if(num1 > num3):
        print("Es mayor el ",num1)
        if (num2 > num3):
            print(" Es menor el ",num3)
        else:
            print(" Es menor el ",num2)
    else:
        if (num2 > num3):
            print("El mayor el ",num1)
            print("El menor el ",num3)
          
        else:
            print("El mayor el ",num3)
            print("El menor el ",num2)
elif (num1 == num2) (and num2 == num3):
    print("Los numeros son iguales")
else:
    if (num3 > num1):
        print(" Es menor el ",num1)
        if (num2 > num3):
            print("El mayor el ",num2)  
        else:
            print("El menor el ",num3)       
    else:
        print(" Es mayor el ",num2)
        print(" Es menor el ",num3)