# Creación del diccionario
dict_youtuber = {}

# Inicialización estática
dict_youtuber["The Grefg"] = ("David", 25, "Andorra", [("Reloj", 3000), ("Pantalón", 1000)])
dict_youtuber["Pereira"] = ("Juan de Pereira", 26, "España", [("Camiseta", 100)])
dict_youtuber["Ibai"] = ("Ibai Juan", 30, "Andorra", [("Zapatillas", 1000), ("Collar", 7000)])


# Comprobamos contenido 
print(dict_youtuber)
print(dict_youtuber.keys())
print(dict_youtuber.values())

# Iteramos las claves
for clave in dict_youtuber.keys():
    print("-", clave)

print("-----")

# Iteramos sus valores
for valor in dict_youtuber.values():
    print("-", valor)

print("\n\n")
# Búsqueda (rápida) por la clave
nombre = input("Nombre del youtuber: ")
if nombre in dict_youtuber:
    valor_tupla = dict_youtuber[nombre]
    nombre, edad, pais, outfit = valor_tupla
    print(f"Pais de {nombre} es {pais}")

print("\n\n")
# Iteramos todos las claves y accedemos a todos sus valores. Mejorable.
print("="*50)
for youtuber in dict_youtuber.keys():
    _, _, pais, _ = dict_youtuber[youtuber]
    print("Pais de", youtuber, "es", pais)

# Iteramos a la par todos las claves y valores. En una sola pasada sin preguntar otra vez al diccionario.
print("="*50)
for youtuber, datos_youtuber in dict_youtuber.items():
    _, _, pais, _ = datos_youtuber
    print("Pais de", youtuber, "es", pais)

# Ejemplo de for sobre variables en una lista
"""
print("="*50)
for elemento in [1, 2, 3, 4]:
    print(elemento)
"""

# Practico con for, _ y range
for _ in range(2):
    print("="*50)

# Ejemplo de for sobre tuplas de 2 elementos en una lista
for elemento1_tupla, elemento2_tupla in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
    print(elemento1_tupla, elemento2_tupla)

for _ in range(2):
    print("="*50)

for youtuber, datos_youtuber in dict_youtuber.items():
    _, _, _, lista_outfit = datos_youtuber
    coste = 0
    #for _, precio in lista_outfit:
    for outfit in lista_outfit:
        _, precio = outfit 
        coste += precio
    print(f"Coste del outfit de {youtuber}: {coste}€")