 #De la siguiente lista, realizar las funciones que obtenga lo siguiente:
 #Obtener el promedio
 #La cantidad de aspirantes que reprobaran

a =[8,9,10,6,6,7,8,9,5,6,7,6,8,8,9,9,5,6,7,9,10,7,8,9,9]


def promedio(lista):
    x = 0
    for i in lista:
        x += i
    y = len(lista)
    prom = x/y
    return print(prom)

def repro(lista):
    reprobados = 0
    for i in lista:
        if i < 6:
            reprobados += 1 
    return print(reprobados)    
        

promedio(a)
repro(a)
