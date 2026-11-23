import random

def sumar(a:int, b:int)->int:
    return a + b

def decir(mensaje:str)->str:
    s = "Mensaje:" + mensaje
    print(s)
    return s
    
def crear_persona()->tuple:
    temp = 4
    nombre = ""
    for _ in range(5):
        nombre += chr(random.randint(temp+65, 90))
    edad = random.randint(10, 50)

    return (nombre.capitalize(), edad)

def print_persona(persona:tuple)->None:
   nombre, edad = persona
   print(f"Nombre: {nombre} - Edad: {edad}")