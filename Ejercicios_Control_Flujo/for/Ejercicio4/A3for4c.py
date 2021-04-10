
def impares(n):

    for i in range(n+1):
        if(i%2!=0):
            print(i)
            if(i == n):
                print("----- FIN ------")

impares(23)
impares(49)
impares(100)

