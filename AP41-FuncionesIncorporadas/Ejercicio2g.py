from itertools import product
def cadenaBase(long,base):
    numsPosibles = []
    for i in product(range(base),repeat=long):
        numsPosibles.append(i)
    for n in numsPosibles:
        print(n)

cadenaBase(3,2)    
    