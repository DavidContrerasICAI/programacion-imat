import funciones 

personas = []
for _ in range(5):
    persona = funciones.crear_persona()
    personas.append(persona)

print(personas)
personas_filtradas = funciones.limpiar_personas(personas)
print(personas)
print(personas_filtradas)

"""
OUTPUT:
print1: [('Zoobu', 28), ('Yjujp', 46), ('Vcaph', 29), ('Sydmy', 34), ('Hrsls', 46)]
print2: [('Zoobu', 28), ('YJUJP', 46), ('Vcaph', 29), ('Sydmy', 34), ('HRSLS', 46)]
print3: [('Yjujp', 46), ('Hrsls', 46)]
"""