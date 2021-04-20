dato1 = [1,None,True,{"clave":"VALOR"}]
dato2  = (2,"hola",False,None)
#dato3 = {1,True,"Hola",[1,2,3]}
dato4 = {"clave":"Valor",1:"clave","dos":2345}

print(all(dato1))
print(all(dato2))
print(all(dato4))

print(any(dato1))
print(any(dato2))
print(any(dato4))