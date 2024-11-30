import funciones as f
from excepciones import *

try:
    asignatura_validada = f.validar_exceptions("DTC-1-1234")
    print(asignatura_validada)
except DepartamentoError as error:
    print("Error por Departamento:", error)
except CursoError as error:
    print("Error por Curso:", error)
except CodigoError as error:
    print("Error por Código:", error)
except ValueError as error:
    print(error)
