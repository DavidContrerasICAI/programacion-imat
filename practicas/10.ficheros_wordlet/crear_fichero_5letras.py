"""
Programa creado únicamente para generar el fichero de palabras de 5 letras
"""

from constantes import *

if __name__ == "__main__":
    mapa_caracteres = {"á":"a", "é": "e", "í": "i", "ó": "o", "ú": "u"}

    fichero = open(FICHERO_PALABRAS, "r", encoding = "utf-8")
    fichero_wordlet = open(FICHERO_PALABRAS_WORDLET, "w", encoding = "utf-8")
    linea = fichero.readline()[:-1]
    while linea:
        if len(linea) == 5:
            acentos = False
            for letra in linea:
                if letra in mapa_caracteres:
                    linea = linea.replace(letra, mapa_caracteres[letra])                

            fichero_wordlet.write(linea + "\n")
        linea = fichero.readline()[:-1]
    fichero.close()
    fichero_wordlet.close()