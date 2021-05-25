def genMultiplos(multiplo=2, emp=1, elem=None):
    """ for emp in range(emp, elem+1, 1):
        if(emp%multiplo == 0):
            yield emp """
    yield [emp for emp in range(emp, elem+1, 1) if(emp%multiplo == 0)]


numeros = genMultiplos(multiplo=7, elem=35)

print(type(numeros))