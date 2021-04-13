fibo = [0,1]
inicio = 0;final = 15

[fibo.append(fibo[elemento-1]+fibo[elemento-2]) for elemento in range(0,15) if elemento > 1]
print(fibo)