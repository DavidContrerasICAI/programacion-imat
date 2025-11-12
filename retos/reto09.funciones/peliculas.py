from funciones import *

if __name__ == "__main__":
    peliculas = crear_diccionario()
    pelis_a1_dict = peliculas["alumno1"]
    pelis_a1_dict["acción"].append(("peli3", 2))

    print()
    print(peliculas)
    print()
    listar_peliculas_alumno(peliculas)
    print()
    agrupar_por_genero(peliculas)