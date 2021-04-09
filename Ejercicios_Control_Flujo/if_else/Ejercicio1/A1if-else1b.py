
dinero = int(input("Cuanto dinero quieres gastar"))

if dinero<100:
    print("pago en efectivo")
elif 100<dinero<300:
    print("pago con debito")
elif dinero>300:
    print("pago con credito")
