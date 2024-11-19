from excepciones import *

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
                try:
                    curso_int = int(curso)
                    if curso_int >= 1 and curso_int <= 4:
                        if not codigo.startswith("12"):
                            raise CodigoError()
                    else:
                        raise CursoError()
                except ValueError as error:
                    raise CodigoError()
            else:
                raise DepartamentoError()

    return "Todo correcto"
