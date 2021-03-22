# num = False;
# print(dir(num));
# print(id(num))
# print(type(num))

import platform
import math as m
#Utilizacion
print("Tiene como documentacion "+platform.__doc__)
print("El sistema operativo es: "+platform.system())
print("El nombre del modulo es: "+platform.__name__)
print("")
print("Las propiedades y métodos de modulo :"+platform.__name__)
print("---------------------------")
pro_met = dir(platform)
print(pro_met)
print("-----------------------")

