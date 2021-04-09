mod = ""
while mod == "":
    si_teclean = input("Teclee algun valor distinto a enter: ")
    print("Valor booleano ",bool(si_teclean))
    if si_teclean:
        mod ="1"
    else:
        print("Por favor tecleen")
