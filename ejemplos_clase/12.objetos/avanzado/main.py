from objetos import *

persona = Persona("Luis", 22)
persona.cumpleanios()

personas = []
try:
    personas.append(Persona("Luis", 0))
except EdadError as error:
    print(error)

try:
    personas.append(Persona("Ana", 33))
except EdadError as error:
    print(error)

try:
    personas.append(Persona("Luisa", 44))
except EdadError as error:
    print(error)

try:
    personas.append(Persona("Jaime", 99))
except EdadError as error:
    print(error)

for persona in personas:
    try:
        persona.cumpleanios()
    except EdadError as error:
        print(error)

    if persona.nombre == "Ana":
        persona.edad += 1
    print(f"{persona.nombre} con edad {persona.edad}")

persona = personas[1]
persona.edad += 1
print(f"{persona.nombre} con edad {persona.edad}")

personas[1].edad += 1
print(f"{personas[1].nombre} con edad {personas[1].edad}")

try:
    persona.cumpleanios()
except EdadError as error:
    print(error)

"""
Ejecutando automáticamente el método __str__
"""
print(personas[1])
print(persona)
