COLA = "_"
CUERPO = "-"
CABEZA = "#"

SERPIENTES = 10
SIZE = 5
velocidad = 0

i = 0
while i < SERPIENTES:
    j = 0
    while j < velocidad:
        print(" ", end="")
        j += 1
    print(COLA, end = "")
    j = 0
    while j < SIZE:
        print(CUERPO, end = "")
        j += 1
    print(CABEZA, end = "")
    print()
    velocidad += 5 + i
    i += 1