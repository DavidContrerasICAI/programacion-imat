"""
ENUNCIADO

Programa una aplicación de consola que gestione outfits de varias personas y calcule el coste total del outfit de una persona concreta.
El programa pedirá primero cuántas personas se van a generar.

Para cada persona:
- Se creará automáticamente un nombre ficticio formado por 4 veces la misma letra mayúscula elegida al azar entre A y K (p. ej., BBBB, JJJJ).
- Se pedirá cuántas prendas tiene esa persona. Para cada prenda, el programa generará aleatoriamente:
    + Un tipo de prenda a partir de la lista fija: ["Bañador", "Pantalón", "Camiseta", "Zapatos", "Falda"].
    + Un precio entero múltiplo de 10, entre 10€ y 100€ (ambos incluidos).
    + Generada una <Prenda> de <Precio>€

Al terminar de crear todas las personas, el programa pedirá el nombre de una persona y calculará el coste total de su outfit (la suma de los precios de sus prendas), mostrando el resultado con el formato:
El coste total del outfit de <Nombre> es <Total>€

Requisitos:
- Utilizar únicamente bucles while para todas las iteraciones (no se permite for).
- Se asume que el nombre introducido al final existe entre las personas generadas.
"""


import random

ROPA = ["Bañador", "Pantalón", "Camiseta", "Zapatos", "Falda"]

personas = []

numero_personas_str = input("Número personas: ")
numero_personas = int(numero_personas_str)
i = 0
while i < numero_personas:
    print()
    nombre = chr(65+random.randint(0, 10)) * 4
    numero_ropa_str = input(f"Número de prendas de {nombre}: ")
    numero_ropa = int(numero_ropa_str)
    ropas = []
    j = 0
    while j < numero_ropa:
        ropa  = ROPA[random.randint(0, len(ROPA)-1)]
        precio = random.randint(1,10) * 10
        ropas.append([ropa, precio])
        print(f"Generada una {ropa} de {precio}€")
        j += 1

    personas.append([nombre, ropas])
    i += 1

#print(personas)
print()

persona_a_buscar = input("Nombre de la persona a calcular el coste de su outfit: ")

i = 0
while i < numero_personas:
    persona_ropa = personas[i]
    nombre = persona_ropa[0]
    # Equivalente a: nombre = personas[i][0]

    if persona_a_buscar == nombre:
        ropa_persona = persona_ropa[1]
        precio_total = 0
        j = 0
        while j < len(ropa_persona):
            precio_total += ropa_persona[j][1]
            j += 1
    i += 1

print(f"El coste total del outfit de {nombre} es {precio_total}€")
