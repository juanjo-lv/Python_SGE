def porc_aprobados(alumnos_aprobados,**aulas):
    total_alumnos = 0
    for i in aulas:
        total_alumnos += aulas[i]

    porcentaje = (alumnos_aprobados/total_alumnos)*100   
    return porcentaje

print(porc_aprobados(100,A=37,B=58,C=40,D=60))