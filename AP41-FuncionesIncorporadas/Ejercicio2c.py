import itertools
tupla = tuple(itertools.combinations('ACTG', 2))
for t in tupla:
    print(t)
