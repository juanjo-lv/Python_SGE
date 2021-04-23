import random
nombres = ["Luis","Rosa","María"]
codigos= ["345F","543D","67FG"]

dic = {random.choice(codigos):elemento for elemento in nombres}
print(dic)

