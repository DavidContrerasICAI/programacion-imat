import funciones as f
from excepciones import *

print("TESTING LISTA Visual")
print("####", f.leer_numeros())

print("TESTING NUMERO")
print(f.validar_numero(5)==None)
try:
    f.validar_numero(4)
except NumeroError as error:
    print(True)

