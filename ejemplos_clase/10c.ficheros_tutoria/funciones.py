def agregar()->None:
    fichero = open("personas.txt", "a")
    fichero.write("Manolo, 34\n")
    fichero.close()

def leer()->dict:
    personas = {}
    fichero = open("personas.txt", "r")
    for linea in fichero:
        linea = linea.strip()
        campos = linea.split(",")
        nombre, edad = campos
        nombre = nombre.strip()
        edad = int(edad.strip())
        personas[nombre] = edad
    fichero.close()   

    return personas


def escribir(personas:dict)->None:
    fichero = open("personas.txt", "w")
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