#import excepciones as ex
from excepciones import *

def validar(asignatura:str) -> bool:
    """
    args:
        asignatura (str):
            "DTC-1-1234"
    """
    error = True
    if len(asignatura) == 10:
        departamento, curso, codigo = asignatura.split("-")
        if len(departamento) == 3 and len(curso) == 1 and len(codigo) == 4:
            if departamento.startswith("D"):
                error = False 
                curso_int = int(curso)
                if curso_int >= 1 and curso_int <= 4:
                    error = False
                    if codigo.startswith("12"):
                        error = False

    return error

def validar_exceptions(asignatura:str) -> str:
    """
    args:
        asignatura (str):
            "DTC-1-1234"
    """

    if len(asignatura) == 10:
        departamento, curso, codigo = asignatura.split("-")
        if len(departamento) == 3 and len(curso) == 1 and len(codigo) == 4:
            if departamento.startswith("D"):
                error = False 
                curso_int = int(curso)
                if curso_int >= 1 and curso_int <= 4:
                    error = False
                    if codigo.startswith("12"):
                        error = False

    if error:
        raise AsignaturaError()
    else:
        return "Todo correcto"
