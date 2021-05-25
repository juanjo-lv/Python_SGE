#imports
import math
import statistics
from collections import OrderedDict 
#declaraciones
x = lambda x : math.pow(x,2)
y = lambda x,y : x+y
z = lambda *x: sum(x)
q = lambda x,y,z : statistics.mean([x,y,z])
r = lambda z : "".join(OrderedDict.fromkeys(z.lower()))



#llamadas
print(x(5)) 
print(y(2,3))
print(z(1,2,3))
print(q(8,10,12))
print(r("EstoesunapruebadeStringformateado"))