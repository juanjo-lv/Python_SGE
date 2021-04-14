listaA = ['A1','A2','A3'];listaB=['B1','B2']

print("Con for normal:")
for a, b in zip(listaA, listaB): 
     print(a,b)
print()

print("Con comprehension:")
[print(a,b) for a,b in zip(listaA,listaB)]