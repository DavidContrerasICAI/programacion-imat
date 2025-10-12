FILAS_MAX = 5
INTENTOS_MAX = FILAS_MAX
LETRAS_POR_PALABRA = 5
CARACTERES_MAXIMOS = FILAS_MAX * LETRAS_POR_PALABRA
CELDA_VACIA = " "

TITULO = r"""
__| |_____________________________________________________________________________________| |__
__   _____________________________________________________________________________________   __
  | |                                                                                     | |  
  | |                                                                                     | |  
  | |      __   __  ___    ______    _______  ________  ___      _______ ___________      | |  
  | |     |"  |/  \|  "|  /    " \  /"      \|"      "\|"  |    /"     "("     _   ")     | |  
  | |     |'  /    \:  | // ____  \|:        (.  ___  :)|  |   (: ______))__/  \\__/      | |  
  | |     |: /'        |/  /    ) :)_____/   ): \   ) ||:  |    \/    |     \\_ /         | |  
  | |      \//  /\'    (: (____/ // //      /(| (___\ ||\  |___ // ___)_    |.  |         | |  
  | |      /   /  \\   |\        / |:  __   \|:       :| \_|:  (:      "|   \:  |         | |  
  | |     |___/    \___| \"_____/  |__|  \___|________/ \_______)_______)    \__|         | |  
  | |                                                                                     | |  
__| |_____________________________________________________________________________________| |__
__   _____________________________________________________________________________________   __
  | |                                                                                     | |  
"""

print(TITULO)

GRIS = "\033[1;47m"
VERDE = "\033[1;42m"
AMARILLO = "\033[1;43m"
DEFECTO = "\033[0m"
ROJO = "\033[0;41m"

PALABRA_OBJETIVO = "ROSAL"
palabra_agrupada = ""
palabra = ""

intentos = 0 
while intentos < INTENTOS_MAX and palabra != PALABRA_OBJETIVO:
    """
    Pide la palabra
    """    
    palabra = input("Palabra: ")
    palabra = palabra.upper()
    palabra_agrupada += palabra
    print()
    indice = 0
    while indice < CARACTERES_MAXIMOS:
        """
        Si hay alguna letra introducida, determino el color. 
        Si no, muestro la casilla vacía.
        """
        if indice < len(palabra_agrupada):
            letra = palabra_agrupada[indice]
            # indice hasta 25, indice_adaptado hasta 5 (palabra_objetivo)
            indice_adaptado = indice - (indice//LETRAS_POR_PALABRA) * LETRAS_POR_PALABRA  
            if letra == PALABRA_OBJETIVO[indice_adaptado]:
                """
                La letra coincide con la misma posición de la palabra objetivo
                """
                color = VERDE
            else:
                """
                ¿La letra está en alguna posición de la palabra objetivo?
                """                  
                indice_letra_amarilla = 0
                is_letra_amarilla = False  # Nos ayuda a saber si habrá alguna letra dentro de la palabra en otra posición
                while indice_letra_amarilla < len(PALABRA_OBJETIVO):
                    if letra == PALABRA_OBJETIVO[indice_letra_amarilla]:
                        is_letra_amarilla = True
                    indice_letra_amarilla += 1
                
                if is_letra_amarilla == True:
                    color = AMARILLO
                else:
                    color = ROJO

            print(f"{color} {letra} {DEFECTO} ", end = "")
        else:
            print(f"{GRIS} {CELDA_VACIA} {DEFECTO} ", end = "") 

        indice += 1  
        
        if indice % LETRAS_POR_PALABRA == 0:
            print("\n")
            
    intentos += 1
        
if palabra == PALABRA_OBJETIVO:
    print("\n¡¡¡Enhorabuena!!!\n")