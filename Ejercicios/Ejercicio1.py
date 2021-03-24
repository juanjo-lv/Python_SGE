from datetime import date, datetime , time , timedelta
import locale,platform

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')

def app():
    nombre = input("¿Cuál es tu nombre?")
    print("hola "+nombre)
    fecha = datetime.now()
    print(f'Estamos a {fecha.strftime("%A").capitalize()}, {fecha.day} de {fecha.strftime("%B")} del año: {fecha.year}')
    print(f"A las {fecha.hour} horas y {fecha.minute} minutos")
    version = platform.python_version()
    print(f"Python {version} es la versión con la que estás trabajando")   
app()
