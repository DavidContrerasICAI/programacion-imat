import funciones 

personas = []
print("ID de personas:", id(personas))
for _ in range(5):
    persona = funciones.crear_persona()
    personas.append(persona)

print(personas)
x = 3
print("ID de X:", id(x))
personas_filtradas = funciones.limpiar_personas(personas, x)
print(personas)
print(personas_filtradas)

nombre_fichero = "personas.txt"
fichero = open(nombre_fichero, "w")    # "r", "w", "a"
for persona in personas: 
    nombre, edad = persona
    fichero.write(f"{nombre}, {edad}\n")
fichero.close()



















"""
OUTPUT:
print1: [('Zoobu', 28), ('Yjujp', 46), ('Vcaph', 29), ('Sydmy', 34), ('Hrsls', 46)]
print2: [('Zoobu', 28), ('YJUJP', 46), ('Vcaph', 29), ('Sydmy', 34), ('HRSLS', 46)]
print3: [('Yjujp', 46), ('Hrsls', 46)]
"""