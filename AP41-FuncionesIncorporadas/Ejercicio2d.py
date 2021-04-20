import itertools
tupla = tuple(itertools.product('123', "ABC"))
for t in tupla:
    print(t)
