import funciones as f
import random

nombres = ["Luis", "Ana", "Pepe", "Jimena"]

dic = {"a":1}
# OPCION 1
if "b" in dic:
    dic["b"]

# OPCIÓN 2
try:
    dic["b"]
except KeyError as error:
    print(error)
    print("Clave no encontrada")

#f.agregar()

personas:list = f.leer()
nombre_random = random.choice(nombres)
edad_random = random.randint(18, 22)
personas[nombre_random] = edad_random
f.escribir(personas)
print(personas)

personas:list = f.leer_pro()
print(personas)
