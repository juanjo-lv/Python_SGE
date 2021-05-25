#Ejercicio 2 apartado a
cadena = 'Examen Python'

print('Que letra desea comprobar ')
letra = input() 

if((letra in cadena) == False): print('La ',letra,' NO ESTA') 
else: print('La ',letra,' ESTA')

#print(f"La letra {variable} está" if (variable in cadena) else f"La letra {variable} no está")
 
 #Ejercicio 2 apartado b
conj = set()

print('Tipo: ',type(conj),' Longitud: ',len(conj))

#Ejercicio 2 apartado c
primero = (3,4,5); segundo = 100; tercero = ["HOLA",{2,4}]

#Ejercicio 3 apartado d
#conjunto = set([(3,4),"hola",5,9,["A","b","c"],"adios",23])

A,B,C = "hola",((3,4),5,9,["A","b","c"],23),"adios"

print(A)
print(B)
print(C)


