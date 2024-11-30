from excepciones import *

def validar_exceptions(asignatura:str) -> str:
    """
    args:
        asignatura (str):
            "DTC-1-1234"
    """

    lista = asignatura.split("-")
    if len(lista) == 3:
        departamento, curso, codigo = lista
        if len(departamento) == 3 and departamento.startswith("D"):
            try:
                curso_int = int(curso)
                if curso_int >= 1 and curso_int <= 4:
                    if len(codigo) >= 2 and len(codigo) <= 4 and codigo.startswith("12"):
                        codigo += "0" * (4 - len(codigo))
                    else:
                        raise CodigoError(f"{codigo} no es válido")
                else:
                    raise CursoError(f"{curso} no es un número")
            except ValueError as error:
                raise CursoError(f"{curso} no es un número")
        else:
            raise DepartamentoError(f"{departamento} no es válido. Debe empezar por D y tener 3 caracteres.")
    else:
        raise ValueError("Debe haber 2 guiones XXX-Y-ZZZZ")

    return departamento, curso_int, codigo
