import funciones as func
import util
#from funciones import crear_persona,limpiar_personas
#from funciones import *

personas = []
for _ in range(5):
    persona = func.crear_persona()
    personas.append(persona)

personas_filtradas = func.limpiar_personas(personas)

#util.crear_fichero(personas, "w")
util.crear_fichero(personas, "w")   # añadiendo

util.decir_hola()
