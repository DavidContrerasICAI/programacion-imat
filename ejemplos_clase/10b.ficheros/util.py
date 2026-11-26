def decir_hola()->None:
    print("HOOOLA")

def crear_fichero(personas:list, opcion:str)->None:
    fichero = open("personas.csv", opcion)    # "r", "w", "a"
    if opcion == "w":
        fichero.write("nombre, edad\n")
    for persona in personas: 
        nombre, edad = persona
        fichero.write(f"{nombre}, {edad}\n")
    fichero.close()