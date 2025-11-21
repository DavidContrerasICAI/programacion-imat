from excepciones import PotenciaError
from constantes import *

def leer_coches()->dict:
    diccionario_coches = {}
    try:
        fichero_error = open("datos/errores.txt", "w", encoding="utf-8")
        for i in range(1, 4):
            nombre_fichero = f"datos/coches{i}.txt"
            fichero = open(nombre_fichero, "r", encoding="utf-8")

            numero_linea_error = 1
            _ = fichero.readline()
            for linea in fichero:
                numero_linea_error += 1
                linea = linea.strip()
                coche, cv_str = linea.split("#")
                try:
                    cv = transformar_cv(cv_str)
                    diccionario_coches[coche] = cv
                except PotenciaError as error:
                    fichero_error.write(f"{nombre_fichero}:{numero_linea_error} <{error}> -> {linea}\n")
                    
            fichero.close()

        fichero_error.close()
    except FileNotFoundError as error:
        print("No se encontró el fichero:", error)

    return diccionario_coches

def guardar_coches(diccionario_coches:dict)->None:
    try:
        with open("datos/coches.csv", "w", encoding="utf-8") as fichero:
            for coche, cv in diccionario_coches.items():
               fichero.write(f"{coche}, {cv}\n")
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
                raise PotenciaError("Potencia inferior a 100cv")
        except ValueError:
            raise PotenciaError("Potencia no numérica")
    else:
        raise PotenciaError("Potencia demasiado larga (+4)")
