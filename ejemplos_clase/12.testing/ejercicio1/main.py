import funciones as f
from constantes import *
import sys


f.inicializar_programa()
lista_numeros = f.leer_numeros()
f.procesar_numeros(lista_numeros)

if len(sys.argv) == 2 and sys.argv[1] == "show": 
    print(lista_numeros)
