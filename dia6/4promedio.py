# Diccionario con nombres y calificaciones
calificaciones = {
    "Alo": 7,
    "Najarro": 8,
    "Meraz": 9,
    "Esperanza": 7,
    "Puebla": 7,
    "Arco": 9,
    "Brazil": 8,
    "Sotomayor": 6,
    "Ortis": 5,
    "Arcos": 7,
    "Borja": 5,
    "Guerrero": 5,
    "Bermejo": 6,
    "Garcia": 7,
    "Ortiz": 8,
    "Mar": 9,
    "Monica": 7,
    "Verdugo": 7,
    "Rossel": 9,
    "Lagunas": 10,
    "Rosado": 10,
    "Pulido": 6,
    "Alvarado": 7,
    "Vea": 8,
    "Lozano": 9,
    "Godinez": 6,
    "Herran": 5,
    "Rengifo": 6,
    "Brizuela": 7,
    "Berlanga": 1
}

# Calcula el promedio de las calificaciones
#promedio = sum(calificaciones.values()) / len(calificaciones)
def promed(lista):
    suma = 0
    for numero in lista:
        suma += lista[numero]
    y = len(lista)
    prom = suma/y
    return prom
# Imprime personas con calificación menor al promedio
print("Personas con calificación menor al promedio:")
for nombre, calificacion in calificaciones.items():
    if calificacion < promed(calificaciones):
        print (nombre,": ",calificacion)
#        print(f"{nombre}: {calificacion}")

# Imprime personas con calificación mayor al promedio
print("\nPersonas con calificación mayor al promedio:")
for nombre, calificacion in calificaciones.items():
    if calificacion > promed(calificaciones):
        print(nombre, ": " ,calificacion)
print ("El promedio del grupo es: ", promed(calificaciones))
