UMBRAL_VALORACION = 5

peliculas = {"alumno1" : { "acción" : [("peli1", 10), ("peli5", 6)],  "terror" : [("peli8", 2), ("peli6", 6)] } , 
             "alumno2" : { "acción" : [("peli3", 8), ("peli7", 2)], "terror" : [("peli8", 2), ("peli6", 6)] } , 
             "alumno3" : { "acción" : [("peli1", 6), ("peli3", 4)], "terror" : [("peli6", 4), ("peli4", 6)] } 
            }

pelis_a1_dict = peliculas["alumno1"]
pelis_a1_dict["acción"].append(("peli3", 2))

print()
print(peliculas)
print()

"""
Listado de películas de un alumno y un género
"""
#nombre = input("Alumno: ")
#genero = input("Género: ")

nombre = "alumno1"
genero = "acción"
if nombre in peliculas:
    dicc_peliculas = peliculas[nombre]
    if genero in dicc_peliculas:
        lista_peliculas = dicc_peliculas[genero]
        print(f"Pelis favoritas de {nombre} valoradas con más de un {UMBRAL_VALORACION}")
        for pelicula in lista_peliculas:
            nombre_pelicula, valoracion = pelicula
            if valoracion > UMBRAL_VALORACION:
                print(f"  - {nombre_pelicula.capitalize()} {valoracion*"⭐"}")
    else:
        print(f"{genero} no existe")
else:
    print(f"{nombre} no existe")

print()

"""
Todas las películas agrupadas por género
Nos apoyaremos en la creación de un nuevo diccionario, ya que es una buena forma de crear agrupaciones
"""
dicc_generos = {}
for alumno, genero_pelis_dict in peliculas.items():
    for genero, peliculas_list in genero_pelis_dict.items():
        if genero not in dicc_generos:
            peliculas_dicc_genero = []
            dicc_generos[genero] = peliculas_dicc_genero
        else:
            peliculas_dicc_genero = dicc_generos[genero]

        for pelicula, valoracion in peliculas_list:
            if pelicula not in peliculas_dicc_genero:
                peliculas_dicc_genero.append(pelicula)


print("Películas agregadas por GÉNERO")

dicc_generos = {}
for alumno, genero_pelis_dict in peliculas.items():
    for genero, peliculas_list in genero_pelis_dict.items():
        if genero not in dicc_generos:
            peliculas_dicc_genero = []
            dicc_generos[genero] = peliculas_dicc_genero
        else:
            peliculas_dicc_genero = dicc_generos[genero]

        for pelicula, valoracion in peliculas_list:
            if pelicula not in peliculas_dicc_genero:
                peliculas_dicc_genero.append(pelicula)

for genero, peliculas_list in dicc_generos.items():
    print(f"🎞️  {genero.capitalize()} 🎞️")
    for pelicula in peliculas_list:
        print(f"  🎥 {pelicula.capitalize()}")

print()

"""
Todas las películas agrupadas por género con las valoracioes medias de todos los usuarios
"""
print("Películas agregadas por GÉNERO con VALORACIONES MEDIAS")

dicc_generos = {}
for alumno, genero_pelis_dict in peliculas.items():
    for genero, peliculas_list in genero_pelis_dict.items():
        if genero not in dicc_generos:
            peliculas_dicc_genero = {}
            dicc_generos[genero] = peliculas_dicc_genero
        else:
            peliculas_dicc_genero = dicc_generos[genero]

        for pelicula, valoracion in peliculas_list:
            if pelicula not in peliculas_dicc_genero:
                peliculas_dicc_genero[pelicula] = [valoracion]
            else:
                peliculas_dicc_genero[pelicula].append(valoracion) 

for genero, peliculas_dict in dicc_generos.items():
    print(f"🎞️  {genero.capitalize()} 🎞️")
    for pelicula, valoraciones in peliculas_dict.items():
        valoracion_suma = 0
        for valoracion in valoraciones:
            valoracion_suma += valoracion
        print(f"  🎥 {pelicula.capitalize()} {int(valoracion_suma/len(valoraciones))*"⭐"} {valoracion_suma/len(valoraciones):.1f}")

print()