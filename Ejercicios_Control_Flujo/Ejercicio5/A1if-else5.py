num1, num2, num3 = 4,3,5

if (num1>num2):
    if(num1 > num3):
        print("Es mayor el ",num1)
        if (num2 > num3):
            print(" Es menor el ",num3)
        elif num2 == num3:
            print("2 y 3 son iguales")
        else:
            print(" Es menor el ",num2)
    else:
        if (num2 > num3):
            print("El mayor el ",num1)
            print("El menor el ",num3)
        elif num2 == num3:
            print("2 y 3 son iguales")    
        else:
            print("El mayor el ",num3)
            print("El menor el ",num2)
elif num1 == num2:
    print(" 1 y 2 son iguales")
else:
    if (num3 > num1):
        print(" Es menor el ",num1)
        if (num2 > num3):
            print("El mayor el ",num2)
        elif num2 == num3:
            print("2 y 3 son iguales")   
        else:
            print("El menor el ",num3)
    elif num3 == num1:
        print("3 y 1 son iguales")        
    else:
        print(" Es mayor el ",num2)
        print(" Es menor el ",num3)