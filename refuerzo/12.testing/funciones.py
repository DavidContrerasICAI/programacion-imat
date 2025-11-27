from excepciones import PotenciaError, PrecioError
from constantes import *

def leer_coches()->dict:
    diccionario_coches = {}
    try:
        fichero_error = open("datos/errores.txt", "w", encoding="utf-8")
        for i in range(1, 4):
            nombre_fichero = f"datos/coches{i}.txt"
            try:
                fichero = open(nombre_fichero, "r", encoding="utf-8")
                numero_linea_error = 1
                _ = fichero.readline()
                for linea in fichero:
                    numero_linea_error += 1
                    linea = linea.strip()
                    coche, cv_str, precio = linea.split(",")
                    coche = coche.strip()
                    cv_str = cv_str.strip()
                    precio = precio.strip()
                    try:
                        precio = transformar_precio(precio)
                        cv = transformar_cv(cv_str)
                        diccionario_coches[coche] = (cv, precio)
                    except PotenciaError as error:
                        fichero_error.write(f"{nombre_fichero}:{numero_linea_error} <{error}> -> {linea}\n")
                        
                fichero.close()
            except FileNotFoundError as error:
                print(error)
        fichero_error.close()
    except ValueError as error:
        print("No se encontró el fichero:", error)

    return diccionario_coches

def guardar_coches(diccionario_coches:dict)->None:
    try:
        with open("datos/coches.csv", "w", encoding="utf-8") as fichero:
            for coche, caracteristicas in diccionario_coches.items():
               cv, precio = caracteristicas
               fichero.write(f"{coche}, {cv}, {precio}\n")
    except FileNotFoundError as error:
        print("No se encontró el fichero:", error)


def transformar_cv(cv_str:str)->int:
    """
    Args:
        - cv_str: potencia en forma de string
    Return:
        - cv: potencia convertida y filtrada
    Raise: 
        - PotenciaError
    """
    if len(cv_str) <= LONGITUD_MAX:
        try:
            cv = int(cv_str)
            if cv >= POTENCIA_MINIMA:
                return cv
            else:
                raise PotenciaError(f"Potencia inferior a {POTENCIA_MINIMA}cv")
        except ValueError:
            raise PotenciaError("Potencia no numérica")
    else:
        raise PotenciaError(f"Potencia demasiado larga (+{LONGITUD_MAX})")


def transformar_precio(precio_str:str) -> int:
    """
    Raises:
        - ValueError

    Examples:
        - xxxxxx
        - 25x00x0  -> 25000
        - 32.000  -> 32000
    """
    precio_transformado = ""
    for digito in precio_str:
        if digito.isdecimal():
            precio_transformado += digito
    
    try:
        precio_valido = int(precio_transformado)
        return precio_valido
    except ValueError as error:
        #raise error
        raise PrecioError("Precio no es numérico")
    

