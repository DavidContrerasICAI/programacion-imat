fichero = open("personas.csv", "r")
cabecera = fichero.readline()    # "nombre, edad"
columna_nombre, columna_edad = cabecera.split(",")
columna_nombre = columna_nombre.strip().capitalize()
columna_edad = columna_edad.strip().capitalize()

suma_edad = 0
personas = 0
for linea in fichero:
    linea = linea.strip()
    nombre, edad = linea.split(",")
    nombre = nombre.strip()
    edad = int(edad.strip())
    suma_edad += edad
    print(f"{columna_nombre}: {nombre} {columna_edad}: {edad}")
    personas += 1

print(f"Personas leida: {personas} con edad media de {suma_edad/personas}")
fichero.close()
