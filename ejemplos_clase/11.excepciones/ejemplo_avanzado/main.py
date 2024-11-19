import funciones as f
from excepciones import *

try:
    output = f.validar_exceptions("DTC-X-1234")
    print(output)
except DepartamentoError as error:
    print("Error por Departamento")
except CursoError as error:
    print("Error por Curso")
except CodigoError as error:
    print("Error por Código")
