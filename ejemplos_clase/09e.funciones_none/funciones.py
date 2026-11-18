import random

def crear_persona()->tuple:
    nombre = ""
    for _ in range(5):
        nombre += chr(random.randint(65, 90))
    edad = random.randint(10, 50)

    return (nombre.capitalize(), edad)

def print_persona(persona:tuple)->None:
   nombre, edad = persona
   print(f"Nombre: {nombre} - Edad: {edad}")