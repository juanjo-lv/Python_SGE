import itertools
nombres = ['Paco','Julia','Javier','Sara','Jose','Gala','Jorge','Ruben','Marta','Alex','Carmen']

valores = itertools.groupby(sorted(nombres,key=len),key=len)

for k,g in valores:
    print(f'Nombres con {k} letras')
    print(f'{list(g)}')


    
