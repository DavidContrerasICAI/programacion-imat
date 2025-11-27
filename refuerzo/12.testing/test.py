import funciones as f
from excepciones import *

VERDE = "\033[1;42m"
DEFECTO = "\033[0m"
ROJO = "\033[0;41m"

print("Testing CV: 12a --> ", end = "")
try:
    cv = f.transformar_cv("12a")
    print(f"{ROJO}False{DEFECTO}")
except PotenciaError as error:
    print(f"{VERDE}True: {error}{DEFECTO}")

print("Testing CV: 120 --> ", end = "")
try:
    cv = f.transformar_cv("120")
    print(f"{VERDE}True: {cv}{DEFECTO}")
except PotenciaError as error:
    print(f"{ROJO}False: {error}{DEFECTO}")

print("Testing PRECIO: 25.000 --> ", end = "")
try:
    precio = f.transformar_precio("25.000")
    print(f"{VERDE}{precio == 25000}: {precio}{DEFECTO}")
except ValueError as error:
    print(f"{ROJO}False{DEFECTO}")

print("Testing PRECIO: xxxxx --> ", end = "")
try:
    precio = f.transformar_precio("xxxxx")
    print(f"{ROJO}False{DEFECTO}")
except PrecioError as error:
    print(f"{VERDE}True: {error}{DEFECTO}")

