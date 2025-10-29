import random
import time

COCHE = "🚗"
CARRETERA = "📔"
ARBOL = "🌴"
HOTEL = "🏨"
EXPLOSION = "💥"

LONGITUD = 10
NUM_ARBOLES = 2

"""
Creación de la carretera
"""
road_list = []
road_list.append(COCHE)
i = 1
while i < LONGITUD -1:
    road_list.append(CARRETERA)
    i += 1
road_list.append(HOTEL)

"""
Colocación de los árboles
"""
num_arbol = NUM_ARBOLES
while num_arbol > 0:
    rnd = random.randint(1,LONGITUD-2)
    if road_list[rnd] == CARRETERA:
        road_list[rnd] = ARBOL
        num_arbol -= 1
"""
Animación del coche
"""
reparando = False    # Cuando el coche se choque contra un árbol, pasará un turno parado en ese punto hasta que se repare
valor_old = CARRETERA
i = 1
while i < len(road_list):
    carretera = ""
    for tramo in road_list:
        carretera += tramo
    print(f"\r{carretera}", end="", flush=True)
    time.sleep(0.5)
    if not reparando:
        road_list[i-1] = valor_old
        valor_old = road_list[i]
        if road_list[i] == ARBOL:
            road_list[i] = EXPLOSION
            reparando = True
        else:
            road_list[i] = COCHE
        i += 1
    else:
        road_list[i-1] = COCHE
        reparando = False
carretera = ""
for tramo in road_list:
    carretera += tramo
print(f"\r{carretera}", end="", flush=True)
time.sleep(0.5)