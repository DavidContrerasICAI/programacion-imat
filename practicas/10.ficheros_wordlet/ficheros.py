from constantes import *
import os.path
import pickle

def leer_palabras() -> list:
    """
    Lee las palabras del fichero

    Returns:
        palabras (list): la palabra elegida
    """
    palabras = []
    existe_fichero = os.path.isfile(FICHERO_PALABRAS_WORDLET)
    if existe_fichero:
        with open(FICHERO_PALABRAS_WORDLET, "r") as fichero:
            palabra = fichero.readline()
            while palabra != "":
                palabras.append(palabra[:-1])
                palabra = fichero.readline()
    
    return palabras


def leer_estadisticas() -> dict:
    estadisticas_dict = {}
    if os.path.isfile(FICHERO_ESTADISTICAS):
        with open(FICHERO_ESTADISTICAS, "rb") as fichero:
            estadisticas_dict = pickle.load(fichero)
    else:
        for fila in range(1, FILAS_MAX+1):
            estadisticas_dict[str(fila)] = 0
        estadisticas_dict["X"] = 0
    
    return estadisticas_dict


def guardar_estadisticas(estadisticas_dict:dict) -> None:
    with open(FICHERO_ESTADISTICAS, "wb") as fichero:
        pickle.dump(estadisticas_dict, fichero)