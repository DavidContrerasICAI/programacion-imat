from constantes import *
import pickle
import os.path

def crear_tablero() -> list:
    """
    Crea la matriz con todas las celdas que contendrán las futuras letras de la palabra con el color pro defecto

    Returns:
        tablero (list): la matriz que representa el tablero
    """
    tablero = []
    for i in range(FILAS_MAX):
        fila = [f"{GRIS} {' '} {DEFECTO} "] * 5
        tablero.append(fila)
    return tablero


def mostrar_tablero(tablero:list) -> None:
    """
    Muestra le tablero

    Args:
        tablero (list): matriz a mostrar
    """
    for fila in tablero:
        for letra in fila:
            print(letra, end = "")
        print("\n")

    return tablero

def letra_exacta(tablero:list, fila:int, col:int, letra:str):
    """
    Asigna una letra que está en la posición correcta en la casilla elegida con el color adecuado

    Args:
        tablero (list): 
        fila (int): 
        col (int): 
        letra (str): 
    """
    tablero[fila][col] = f"{VERDE} {letra} {DEFECTO} "

def letra_no_exacta(tablero:list, fila:int, col:int, letra:str):
    """
    Asigna una letra que pertenece a la palabra en la casilla elegida con el color adecuado

    Args:
        tablero (list): 
        fila (int): 
        col (int): 
        letra (str): 
    """
    tablero[fila][col] = f"{ROJO} {letra} {DEFECTO} "

def letra_no_esta(tablero:list, fila:int, col:int, letra:str):
    """
    Asigna una letra que no pertenece a la palabra en la casilla elegida con el color adecuado

    Args:
        tablero (list): 
        fila (int): 
        col (int): 
        letra (str): 
    """
    tablero[fila][col] = f"{NEGRO_FOREGROUND}{GRIS} {letra} {DEFECTO} "

def leer_palabras() -> list:
    """
    Elige una palabra aleatoria de todo el fichero de palabras de 5 letras

    Returns:
        palabra (str): la palabra elegida
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
    with open(FICHERO_ESTADISTICAS, "rb") as fichero:
        estadisticas_dict = pickle.load(fichero)
        return estadisticas_dict

def guardar_estadisticas(estadisticas_dict:dict) -> None:
    with open(FICHERO_ESTADISTICAS, "wb") as fichero:
        pickle.dump(estadisticas_dict, fichero)

def mostrar_estadisticas(estadisticas_dict) -> None:
    print("Estadísticas")
    for intentos, veces in estadisticas_dict.items():
        casilla = f"{GRIS}  {DEFECTO}"
        print(f"{intentos} {casilla * veces}")
        
