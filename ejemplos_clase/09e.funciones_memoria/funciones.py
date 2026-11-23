import random

def crear_persona()->tuple:
    nombre = ""
    for _ in range(5):
        nombre += chr(random.randint(65, 90))
    edad = random.randint(10, 50)

    return (nombre.capitalize(), edad)

def limpiar_personas(personas:list, x:int)->list:
    print("ID de personas en función:", id(personas))
    x = x + 1
    print("ID de X en función:", id(x))
    personas_filtradas = []
    i = 0
    for persona in personas:
        nombre, edad = persona
        if edad > 35:
            personas_filtradas.append(persona)
            personas[i] = (nombre.upper(), edad)
        i += 1

    return personas_filtradas