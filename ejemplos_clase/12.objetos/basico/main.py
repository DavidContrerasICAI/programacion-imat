from objetos import *

"""
Ejemplo de detección de tipos por duda planteada en clase
"""
def mostrar_persona3(persona:Persona):
    if isinstance(persona, Persona):
        print(f"Mostrando persona: {persona.nombre} - {persona.edad}")

def mostrar_persona2(persona:Persona):
    tipo_persona = type(persona)
    if tipo_persona.__name__ == "Persona":
        print(f"Mostrando persona: {persona.nombre} - {persona.edad}")

def mostrar_persona1(persona:Persona):
    if "Persona" in str(type(persona)):
        print(f"Mostrando persona: {persona.nombre} - {persona.edad}")


"""
Ejemplo co tuplas
"""
persona_tupla = ("Luis", 22)
print(persona_tupla)
nombre, edad = persona_tupla
print(nombre, edad)
print(type(persona_tupla))

"""
Mismo con objetos
"""
persona = Persona("Luis", 22)
print(type(persona))

print(persona.nombre, persona.edad)

mostrar_persona1(persona)
mostrar_persona2(persona)
mostrar_persona3(persona)

"""
persona2 = Persona("Luis", 22)
persona3 = Persona("Ana", 33)
persona4 = Persona("Luisa", 44)
persona5 = Persona("Jaime", 55)

print(persona3.nombre, persona3.edad)
print(persona4.nombre, persona4.edad)
print(persona5.nombre, persona5.edad)
"""

personas = []
personas.append(Persona("Luis", 22))
personas.append(Persona("Ana", 33))
personas.append(Persona("Luisa", 44))
personas.append(Persona("Jaime", 55))

for persona in personas:
    if persona.nombre == "Ana":
        persona.edad += 1
    print(f"{persona.nombre} con edad {persona.edad}")

persona = personas[1]
persona.edad += 1
print(f"{persona.nombre} con edad {persona.edad}")

personas[1].edad += 1
print(f"{personas[1].nombre} con edad {personas[1].edad}")

print(f"{personas[1].nombre} con edad {personas[1].edad}")
