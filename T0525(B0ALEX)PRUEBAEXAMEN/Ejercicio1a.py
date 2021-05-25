
print('--- normal ---')
num_impares = []
num_mult_tres = []
num_impares_mult_tres = []

for i in range(20):
    if(i%2 !=0):
        num_impares.append(i)

print(num_impares)

for i in range(20):
    if(i%3 == 0):
        num_mult_tres.append(i)

print(num_mult_tres)


for i in range(20):
    if(i%2 !=0 and i%3 == 0):
        num_impares_mult_tres.append(i)

print(num_impares_mult_tres)
print('--- comprehension ---')

num_impares.clear()
num_mult_tres.clear()
num_impares_mult_tres.clear()

num_impares = [i for i in range(20) if i%2 !=0]
print(num_impares)

num_mult_tres = [i for i in range(20) if i%3 == 0]
print(num_mult_tres)

num_impares_mult_tres = [i for i in range(20) if i%2 != 0 and i%3 == 0]
print(num_impares_mult_tres)


def hola(nombre):
    print(f'hola {nombre}')