"""
Solución al examen inter con DICCIONARIOS
Author: David Contreras
Date: 2/nov
Changed: 2/nov
Version: 3.11 
"""

from funciones import *
# import funciones
# import funciones as f


"""
Función MAIN
"""
if __name__ == "__main__":    # equivaldía a def main():
    cadena = "adcdabbdbcdbdc"
    cadena = "carlacaca"

    print("Cadena de entrada:", cadena)

    frecuencias_dict = identificacion_caracteres_unicos(cadena)
    frecuencias_sorted = ordenar(frecuencias_dict)
    calculo_frecuencias(frecuencias_dict, frecuencias_sorted)


