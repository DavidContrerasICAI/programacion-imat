from constantes import *
import funciones as func

def jugar(palabras:list, palabra_objetivo:str, version:str="PRO") -> int:
    # Creación y mostrar el tablero 
    tablero = func.crear_tablero()
    func.mostrar_tablero(tablero)

    intentos = 0 
    contador_palabras_ok = 0
    while intentos < INTENTOS_MAX and contador_palabras_ok < NUMERO_LETRAS:
        contador_palabras_ok = 0

        # La palabra debe existir y ser de N (5) letras
        palabra = input("Tu palabra: ")
        while palabra.lower() not in palabras or len(palabra) != NUMERO_LETRAS:
            print(f">>> {palabra} NO válida")
            palabra = input("Tu palabra: ")
        
        palabra_introducida = palabra.upper()

        if version == "PRO":
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

            if version == "PRO":
                if letra in dict_letras:
                    if letra != palabra_objetivo[indice] and dict_letras[letra] > 0:
                        func.letra_no_exacta(tablero, intentos, indice, letra)
                else:
                    func.letra_no_esta(tablero, intentos, indice, letra)
            else:
                if letra == palabra_objetivo[indice]:
                    func.letra_exacta(tablero, intentos, indice, letra)
                elif letra in palabra_objetivo:
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
        fila_acierto = "X"
    else:
        fila_acierto = str(intentos) 

    return fila_acierto