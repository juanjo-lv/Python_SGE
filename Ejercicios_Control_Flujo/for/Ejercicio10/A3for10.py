#Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.

def app():
    valores = int(input("¿Cuántos valores va a introducir? "))
    if valores < 1:
        print("numero no valido")
    else:
        anterior = int(input("Escriba un número: "))
        for i in range(valores - 1):
            numero = int(input(f"Escriba un número más grande que {anterior}: "))
            if numero <= anterior:
                print(f"¡{numero} no es mayor que {anterior}!")
            anterior = numero
        print("Hemos terminado")

app()
