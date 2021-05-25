def elemento_quimico(simbolo):
    dic = {
        "He": "Helio-2",
        "O" : "Oxigeno-8",
        "S" : "Azufre-16",
        "Au" : "Oro-79",
        "N"  : "Nitrogeno-7"
    }

    for clave,valor in dic.items():
        if(clave==simbolo):
            numero =  valor.split("-")
            nombre = numero[0]
            numAt = numero[1]

    print(f"Numero Atómico de {nombre} es: {numAt}")
elemento_quimico("Au")
