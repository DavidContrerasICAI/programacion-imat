from constantes import *
import funciones as func
import ficheros as file
import sys
import random
import juego



if __name__ == "__main__":
    # Lectura del fichero y selección de la palabra objetivo 
    palabras = file.leer_palabras()
    if len(palabras) > 0:
        posicion = random.randint(0, len(palabras)-1)
        palabra_objetivo = palabras[posicion].upper()
    else:
        print("Fichero de palabras no encontrado, se utilizará una palabra fija")
        palabra_objetivo = PALABRA_POR_DEFECTO

    # Si se ejecuta como "python wordlet.py 1", se mostrará la palabra objetivo
    if len(sys.argv) == 2 and sys.argv[1] == MOSTRAR_PALABRA_OBJETIVO:
        print(palabra_objetivo)

    # Creación del dict de estadísticas
    estadisticas_dict = file.leer_estadisticas()

    # Juego del Wordlet propiamente dicho
    fila_acierto = juego.jugar(palabras, palabra_objetivo)

    estadisticas_dict[str(fila_acierto)] += 1

    func.mostrar_estadisticas(estadisticas_dict)
    file.guardar_estadisticas(estadisticas_dict)