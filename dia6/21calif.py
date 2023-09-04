# Lista de usuarios y calificaciones
usuarios_calificaciones = [
    ("Roman Alo", 7),
    ("Eliazar Najarro", 8),
    ("Cristofer Meraz", 9),
    ("Salvatore Esperanza", 7),
    ("Marquez Puebla", 7),
    ("Jeremias Arco", 9),
    ("Nestor Brazil", 8),
    ("Carmelita Sotomayor", 6),
    ("Orlin Ortis", 5),
    ("Cris Arcos", 7),
    ("Carlos Borja", 5),
    ("Casimiro Guerrero", 5),
    ("Larunda Bermejo", 6),
    ("Marissa Garcia", 7),
    ("Honoratas Ortiz", 8),
    ("Isidora Mar", 9),
    ("Aletea Monica", 7),
    ("Estefana Verdugo", 7),
    ("Carmita Rossel", 9),
    ("Cesara Lagunas", 10),
    ("Rosemarie De la Rosa", 10),
    ("Garbine Pulido", 6),
    ("Carmelita Alvarado", 7),
    ("Faqueza Vea", 8),
    ("Daunte Lozano", 9),
    ("Leonardo Godinez", 6),
    ("Cesar Herran", 5),
    ("Alfredo Rengifo", 6),
    ("Cristobal Brizuela", 7),
    ("Alvar Berlanga", 10),
]

# Usuarios con calificación perfecta (10)
usuarios_calificacion_perfecta = [usuario for usuario, calificacion in usuarios_calificaciones if calificacion == 10]

# Usuarios con calificación reprobatoria (menos de 6)
usuarios_calificacion_reprobatoria = [usuario for usuario, calificacion in usuarios_calificaciones if calificacion < 6]

# Usuarios cuyos nombres comienzan con "Ca"
usuarios_nombre_comienza_con_Ca = [usuario for usuario, _ in usuarios_calificaciones if usuario.startswith("Ca")]

# Imprimir los resultados
print("Usuarios con calificación perfecta (10):")
for usuario in usuarios_calificacion_perfecta:
    print(usuario)

print("\nUsuarios con calificación reprobatoria:")
for usuario in usuarios_calificacion_reprobatoria:
    print(usuario)

print("\nUsuarios cuyos nombres comienzan con 'Ca':")
for usuario in usuarios_nombre_comienza_con_Ca:
    print(usuario)
