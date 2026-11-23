fichero = open("personas.txt", "r")
for linea in fichero:
    linea = linea.strip()
    print(linea)

fichero.close()
