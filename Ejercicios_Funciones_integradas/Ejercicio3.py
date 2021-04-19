#eval -> Ejecuta una sentencia de una linea si es legal en Python
#exec -> Ejecuta un bloque de codigo multilinea si es legal en Python


eval("print('holaMundo')");
eval("print(3+2)")
eval("exec('a = 3;b= 5;c = a+b;print(c)')")

x ='''
a = 5
b = 6
c = a -b
print(c)
'''
exec(x)

y = '''
palabra = input("Introduce una palabra")
n = int(input("introduce un numero"))
print(palabra*n)

'''

exec(y)