from excepciones import CoordenadasError
from constantes import *
import random

matriz = []

def parsear_destino(coordenadas_destino_str):
    coordenadas_destino_str = coordenadas_destino_str.replace(" ", "")
    if coordenadas_destino_str.count(",") == 1:
        coordenadas = coordenadas_destino_str.split(",")
        try:
            x = int(coordenadas[0])
            y = int(coordenadas[1])

            if (x < 0 or x > FILAS - 1) or (y < 0 or y > COLUMNAS - 1):
                raise CoordenadasError(f"Las coordenadas deben estar entre x:{FILAS} y y:{COLUMNAS}")    
        except ValueError as error:
            raise CoordenadasError("No contiene números")
    else:
        raise CoordenadasError("No contiene comas")

    return x, y

def generar_random():
    return random.randint(0, FILAS - 1), random.randint(0, COLUMNAS - 1)

def borrar_en_ciudad(objeto):
    global matriz
    matriz[objeto.x][objeto.y] = None

def posicionar_en_ciudad(objeto):
    global matriz
    matriz[objeto.x][objeto.y] = objeto

def init_ciudad():
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append(None)
        matriz.append(fila)

def print_ciudad():
    print(f" " * 4, end="")

    for i in range(len(matriz)):
        print(f"    {i}     ", end="")

    print()

    numero = 0
    for fila in matriz:
        print(f" {numero}  ", end = "")
        numero += 1
        for columna in fila:
            if columna != None:
                print(columna.print_in_ciudad(), end = "")
            else:
                print(CHAR_VACIO, end = "")
        print()

    print()