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
    if velocidad <= 10:
        velocidad += 5
    else:
        velocidad -= 5
    
    print(COLA, end = "")
    j = 0
    while j < SIZE:
        print(CUERPO, end = "")
        j += 1
    print(CABEZA, end = "")
    print()
    i += 1