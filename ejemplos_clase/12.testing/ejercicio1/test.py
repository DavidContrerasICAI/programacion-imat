import funciones as f
from excepciones import *

print("TESTING LISTA Visual")
#print("####", f.leer_numeros())

print("TESTING NUMERO")
#print(f.validar_numero(5)==6)

try:
    f.validar_numero(4)
except NumeroError as error:
    print(True)
except:
    print(False)

