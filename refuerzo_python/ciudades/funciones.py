from constantes import NUMERO_CAMPOS, EDAD_MAX, EDAD_MIN, dict_cp
import re


def sumar(a:int, b:int, c:int=10)->int:
    return a + b + c

def sumar2(*numeros)->int:
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def validar_linea_persona(personas_limpias:list, linea:str)->bool:  
    """
    Docstring

    @Args

    @Return
        True: si se ha realizado la validación OK
        False: alguna regla se incumplió

    """
    validacion = True
    patron = r"^(?:Calle|Avenida)\s+.+,\s*\d+$"

    contador_error = 0
    campos = linea.split(";")      
    if len(campos) == NUMERO_CAMPOS:
        nombre, edad, direccion, cp, ciudad = linea.split(";")
        edad = int(edad)
        ciudad = ciudad.strip()
        if edad >= EDAD_MIN and edad < EDAD_MAX:
            dict_valor = dict_cp[ciudad]
            if cp.startswith(dict_valor):
                cp = int(cp)
                if re.match(patron, direccion, re.IGNORECASE):
                    personas_limpias.append((nombre, edad, direccion, cp, ciudad))   
                else:
                    validacion = False
                    print(f">>> Error #8899: dirección no es correcta: ", direccion)
            else:
                validacion = False
                print(f">>> Error #001: el cp {cp} no se corresponde con la ciudad {ciudad} -->", linea)
        else:
            validacion = False
            print(">>> Error #982: edad no válida -->", linea)
    else:
        validacion = False
        print(">>> Error #435: faltan datos -->", linea)

    return validacion


def validar_linea_persona_exception(personas_limpias:list, linea:str)->bool:  
    """
    Docstring

    @Args

    @Return
        True: si se ha realizado la validación OK
        False: alguna regla se incumplió

    """
    validacion = True
    patron = r"^(?:Calle|Avenida)\s+.+,\s*\d+$"

    contador_error = 0
    campos = linea.split(";")      
    if len(campos) == NUMERO_CAMPOS:
        nombre, edad, direccion, cp, ciudad = linea.split(";")
        edad = int(edad)
        ciudad = ciudad.strip()
        if edad >= EDAD_MIN and edad < EDAD_MAX:
            dict_valor = dict_cp[ciudad]
            if cp.startswith(dict_valor):
                cp = int(cp)
                if re.match(patron, direccion, re.IGNORECASE):
                    personas_limpias.append((nombre, edad, direccion, cp, ciudad))   
                else:
                    raise ValueError("Error #8899: dirección no es correcta." + direccion)
            else:
                raise ValueError(f"Error #001: el cp {cp} no se corresponde con la ciudad {ciudad} -->" + linea)
        else:
            raise ValueError("Error #982: edad no válida -->" + linea)
    else:
        raise ValueError("Error #435: faltan datos -->" + linea)

    return validacion
