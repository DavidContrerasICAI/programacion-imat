def agregar()->None:
    fichero = open("personas.txt", "a")
    fichero.write("Manolo, 34\n")
    fichero.close()

def leer()->dict:
    personas = {}
    try:
        fichero = open("personas_file.txt", "r")
        for linea in fichero:
            linea = linea.strip()
            campos = linea.split(",")
            nombre, edad = campos
            nombre = nombre.strip()
            edad = int(edad.strip())
            personas[nombre] = edad
        fichero.close()   
    except FileNotFoundError as error:
        print(error)
        print("Fichero \"personas.txt\" encontrado")

    return personas


def escribir(personas:dict)->None:
    import os

    EXTENSION = ".txt"
    contador = 0
    nombre_fichero = "personas" 
    existe = os.path.isfile(nombre_fichero + EXTENSION)
    nombre_fichero += str(contador) 
    while existe:
        longitud_contador = len(str(contador))
        nombre_fichero = nombre_fichero[:-longitud_contador]
        contador += 1
        nombre_fichero += str(contador)
        existe = os.path.isfile(nombre_fichero + EXTENSION)    

    fichero = open(nombre_fichero + EXTENSION, "w")
    for nombre, edad in personas.items():
        fichero.write(f"{nombre}, {edad}\n")
    fichero.close()   

def leer_pro()->dict:
    personas = {}
    #fichero = open("personas_chat.txt", "r", encoding="utf-8")
    with open("personas_chat.txt", "r", encoding="utf-8") as fichero:
        linea = fichero.readline()
        linea = fichero.readline()
        fichero.readline()
        for linea in fichero:
            linea = linea.strip()
            campos = linea.split("|")
            _, nombre, edad, _ = campos
            nombre = nombre.strip()
            edad = edad.strip()
            edad, _ = edad.split(" ")
            edad = int(edad.strip())
            personas[nombre] = edad
    #fichero.close()   

    return personas