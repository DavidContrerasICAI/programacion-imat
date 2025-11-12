lista_fichero = []
with open("personas.txt", "r") as fichero:
    lista_fichero = fichero.readlines()

print(lista_fichero)

personas = {}
i = 0
while i < len(lista_fichero):
    nombre = lista_fichero[i].rstrip()
    edad = int(lista_fichero[i+1].rstrip())
    ciudad = lista_fichero[i+2].rstrip()

    personas[nombre] = (edad,ciudad)

    i += 3

print(personas)

