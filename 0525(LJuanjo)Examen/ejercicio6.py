def pino(tam, adornos="@"):
   
    print("*".center(tam))
    for i in range(1,tam,2):
        print((adornos*i).center(tam))
    print("|".center(tam))   

print(pino(15))