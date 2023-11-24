from constantes import *
import funciones as func
import random
import sys

if __name__ == "__main__":
    # Si se ejecuta como "python wordlet.py 1", se mostrará la palabra objetivo
    if len(sys.argv) == 2 and sys.argv[1] == "1":
        MOSTRAR_SOLUCION = True
    else:
        MOSTRAR_SOLUCION = False
    
    # Lectura del fichero y selección de la palabra objetivo 

    palabras_diccionario = func.leer_palabras()
    if len(palabras_diccionario) > 0:
        posicion = random.randint(0, len(palabras_diccionario)-1)
        palabra_objetivo = palabras_diccionario[posicion].upper()
    else:
        print("Fichero de palabras no encontrado, se utilizará una palabra fija")
        palabra_objetivo = "ROSAL"

    if MOSTRAR_SOLUCION:
        print(palabra_objetivo)

    # Creación y mostrar el tablero 
    tablero = func.crear_tablero()
    func.mostrar_tablero(tablero)

    # Creación del dict de estadísticas
    try:
        estadisticas_dict = func.leer_estadisticas()
    except:
        estadisticas_dict = dict()
        for fila in range(1, FILAS_MAX+1):
            estadisticas_dict[str(fila)] = 0
        estadisticas_dict["X"] = 0

    intentos = 0 
    contador_palabras_ok = 0
    while intentos < INTENTOS_MAX and contador_palabras_ok < NUMERO_LETRAS:
        contador_palabras_ok = 0

        # La palabra debe existir y ser de N (5) letras
        palabra = input("Tu palabra: ")
        while palabra.lower() not in palabras_diccionario or len(palabra) != NUMERO_LETRAS:
            print(f">>> {palabra} NO válida")
            palabra = input("Tu palabra: ")
        
        palabra_introducida = palabra.upper()

        # Se crea un dict con la frecuencia de las letras de la palabra objetivo, para dar prioridad
        # a las letras colocadas exactamente en su posición
        dict_letras = dict()
        for letra in palabra_objetivo:
            if letra in dict_letras:
                dict_letras[letra] = dict_letras[letra] + 1
            else:
                dict_letras[letra] = 1

        # Identifica las letras perfectamente colocadas y las resta del diccionario de frecuencias
        indice = 0
        while indice < len(palabra_introducida):
            letra = palabra_introducida[indice]
            if letra == palabra_objetivo[indice]:
                func.letra_exacta(tablero, intentos, indice, letra)
                dict_letras[letra] = dict_letras[letra] - 1
                contador_palabras_ok += 1
            else:
                func.letra_no_esta(tablero, intentos, indice, letra)
            
            indice += 1

        # Cuando se han identificado las letras exactas, vamos a ver si hay otras que no lo están, siempre que no existan en el diccionario (> 0)
        indice = 0
        while indice < len(palabra_introducida):
            letra = palabra_introducida[indice]
            if letra in dict_letras:
                if letra != palabra_objetivo[indice] and dict_letras[letra] > 0:
                    func.letra_no_exacta(tablero, intentos, indice, letra)
            else:
                func.letra_no_esta(tablero, intentos, indice, letra)
            indice += 1

        print("\n")
        func.mostrar_tablero(tablero)

        intentos += 1
        
    if contador_palabras_ok == NUMERO_LETRAS:
        print("\n¡¡¡Enhorabuena!!!\n")
    else:
        print(f"\nOhhhhh! Lo siento\nPalabra: {palabra_objetivo}\n")

    if intentos + 1 > NUMERO_LETRAS:
        fila = "X"
    else:
        fila = str(intentos) 
    estadisticas_dict[str(fila)] += 1

    func.mostrar_estadisticas(estadisticas_dict)

    func.guardar_estadisticas(estadisticas_dict)