import random

TITULO = r"""
   ___     ____      __  __      ___      ___   
  F _ ",  F __ ]    F  \/  ]    F _ ",   F __". 
 J `-'(| J |--| L  J |\__/| L  J `-'(|  J (___| 
 | ,--.\ | |  | |  | |`--'| |  | ,--.\  J\___ \ 
 F L__J \F L__J J  F L    J J  F L__J \.--___) \
J_______J\______/FJ__L    J__LJ_______JJ\______J
|_______FJ______F |__L    J__||_______F J______F
"""

GRIS = "\033[1;47m"
VERDE = "\033[1;42m"
DEFECTO = "\033[0m"
ROJO = "\033[0;41m"
AMARILLO = "\033[1;43m"

SIZE = 4
NUM_BOMBAS = 3

BOMBA = "B"
PREMIO = "P"
CASI = "·"


print(TITULO)


########################### 
#   Crear tablero
###########################

matriz = []
i = 0
while i < SIZE:
    columnas = []
    j=0
    while j < SIZE:
        columnas.append(" ")
        j += 1
    matriz.append(columnas)
    i += 1
 
########################### 
#   Asignación de objetos
###########################

n = 4

k = 0
while k < NUM_BOMBAS:
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)
    matriz[i][j] = BOMBA
    k += 1

i = random.randint(0,n-1)
j = random.randint(0,n-1)
while matriz[i][j] == BOMBA:
    i = random.randint(0,n-1)
    j = random.randint(0,n-1)

matriz[i][j] = PREMIO


########################### 
#   Juego
###########################

fin = False
while not fin:
    x = -1
    y = -1
    while not (x >= 0 and x < n) or not (y >= 0 and y < n): 
        print() 
        x = int(input(f"Coordenada X [0, {SIZE}]: "))
        y = int(input(f"Coordenada Y [0, {SIZE}]: "))

    if matriz[x][y] != BOMBA and matriz[x][y] != PREMIO:
        matriz[x][y] = CASI
        print("Sigue jugando...")
    else:
        fin = True

if matriz[x][y] == PREMIO:
    print("\nWIN\n")
else:
    print("\nLOSE\n")


########################### 
#   Mostrar tablero
###########################

i = 0
while i < len(matriz):
    j=0
    while j < len(matriz[i]):
        if matriz[i][j] == BOMBA:
            color = ROJO
        elif matriz[i][j] == PREMIO:
            color = VERDE
        elif matriz[i][j] == CASI:
            color = AMARILLO
        else:
            color = GRIS
        if x == i and y == j:
            efecto = "<>"
        else:
            efecto = "  "

        print(f"{color}{efecto[0]}{matriz[i][j]}{efecto[1]}{DEFECTO} ", end="")
        j += 1
    print("\n")
    i += 1 