#Del siguiente diccionario realizar las funciones que obtenga lo sguiente:
#obtener el promedio
#El/los aspirante(s) con mayor calificacion y con menor calificacion 

alumnos = {
    "Juan":8,
    "Giselle":9,
    "Damian":5,
    "Ricardo":6,
    "Yaotzin":6,
    "Erick":7,
    "Mario":8,
    "Edgar":9,
    "Fernanda":5,
    "Daniel":6,
    "Jesus":7,
    "Damian":8,
    "Yemahina":6,
    "Eduardo":9,
    "Bryan":9,
    "Mariano":10,
    "Alberto":8
}

def promedio(lista):
    suma = 0
    for numero in lista:
        suma += lista[numero]
    y = len(lista)
    prom = suma/y
    return print (prom)

def may(lista):
    x = 0
    for num in alumnos:
        x = alumnos[num]
        if (alumnos[num] == 10 ):
            y = print ("El alumno con mayor calificación es: " + str(num))
    return y
def men(lista):
    x = 0
    for num in alumnos:
        x =+ alumnos[num]
        if (alumnos[num] == 5 ):
            y = print ("El alumno con menor calificación es: " + str(num))
    return y

promedio(alumnos)
may(alumnos)
men(alumnos)