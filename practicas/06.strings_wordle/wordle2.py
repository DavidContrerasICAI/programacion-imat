FILAS_MAX = 5
INTENTOS_MAX = FILAS_MAX
LETRAS_POR_PALABRA = 5
CARACTERES_MAXIMOS = FILAS_MAX * LETRAS_POR_PALABRA
CELDA_VACIA = " "

TITULO = r"""
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
                                                   
"""

print(TITULO)

GRIS = "\033[1;47m"
VERDE = "\033[1;42m"
AMARILLO = "\033[1;43m"
DEFECTO = "\033[0m"
ROJO = "\033[0;41m"

LETRAS = 5

PALABRA_OBJETIVO = "ROSAL"
palabra_vacia = " " * LETRAS
palabra_agrupada = ""
intentos = 0 
palabra = ""

while intentos < INTENTOS_MAX and palabra != PALABRA_OBJETIVO:
    """
    Pide la palabra
    """    
    palabra = input("Palabra: ")
    palabra = palabra.upper()
    palabra_agrupada += palabra
    print()

    """
    Muestra el tablero con palabras introducidas
    """
    filas_introducidas = 0
    num_palabras_introducidas = len(palabra_agrupada)//LETRAS

    while filas_introducidas < num_palabras_introducidas:
        i = filas_introducidas * LETRAS
        j = (filas_introducidas + 1) * LETRAS
        palabra_introducida = palabra_agrupada[i:j]

        indice = 0
        contador_ok = 0
        while indice < len(palabra_introducida):
            """
            Valida la palabra
            """   
            letra = palabra_introducida[indice]
            if letra == PALABRA_OBJETIVO[indice]:
                color = VERDE
                contador_ok += 1
            else:
                if letra in PALABRA_OBJETIVO:
                    color = AMARILLO
                else:
                    color = ROJO
            # Imprime la palabra introducida con los aciertos o no
            print(f"{color} {letra} {DEFECTO} ", end = "")
            indice += 1
            
        print("\n")
        filas_introducidas += 1
        
    """
    Muestra el tablero vacío
    """
    filas = filas_introducidas
    while filas < FILAS_MAX:
        for letra in palabra_vacia:
            print(f"{GRIS} {letra} {DEFECTO} ", end = "")
        print("\n")
        filas += 1
   
    intentos += 1
    
if palabra == PALABRA_OBJETIVO:
    print("\n¡¡¡Enhorabuena!!!\n")