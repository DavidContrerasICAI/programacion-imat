def decir_hola()->None:
    print("HOOOLA")

def crear_fichero(personas:list)->None:
    fichero = open("personas.txt", "w")    # "r", "w", "a"
    for persona in personas: 
        nombre, edad = persona
        fichero.write(f"{nombre}, {edad}\n")
    fichero.close()