import funciones as f
from excepciones import *

try:
    output = f.validar_exceptions("XTC-1-1234")
    print(output)
except AsignaturaError as error:
    print("Error de asignatura")
