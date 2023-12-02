import sys
import funciones as f

"""
Programa de Data Wrangling sobre un fichero de ordenadores 

Run as:
    > python main.py Lenovo
"""

if __name__ == "__main__":
    if len(sys.argv) == 2:
        marca = sys.argv[1]

        ordenadores_dict = {}
        ordenadores = f.inicializar_datos()
        for ordenador_str in ordenadores:
            try:
                ordenador = f.limpiar_datos_objetos(ordenador_str)
                if ordenador.marca in ordenadores_dict:
                    lista = ordenadores_dict[ordenador.marca]
                    lista.append(ordenador)
                else:
                    lista = [ordenador]
                    ordenadores_dict[ordenador.marca] = lista
            except Exception as error:
                print(f"No se puedo procesar la entrada: {ordenador_str}", error)
        print(f"Ordenadores {marca}:")
        if marca in ordenadores_dict:
            ordenadores = ordenadores_dict[marca] 
            for ordenador in ordenadores:
                print(f"- {ordenador}")
        else:
            print("- No se encontró ninguno")
    else:
        print("El programa debe indicar la marca de ordenador a buscar")
        print("Ejemplo: python main.py Lenovo")
