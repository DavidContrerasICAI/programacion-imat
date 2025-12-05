import random
from constantes import *
from excepciones import *


def inicializar_programa()->str:
    s = "assasa" + 21121

    # "as344Ya" ---> "344Y"

    # No me funciona
    return "344Y"



def procesar_numeros(numeros:list[int]):
    pass    # ToDo

def leer_numeros()->list[int]:
    lista = []
    for i in range(10):
        numero = random.randint(1, 9)
        try:
            numero =validar_numero(numero)
            lista.append(numero)
        except NumeroError as error:
            print(">>>>>", error)
    return lista

def validar_numero(numero:int)->int:
    """
    Comprueba que numero es superior al NUMERO_CORTE

    Raises:
        - NumeroError
    Examples:
        - 3 raises NumeroError
        - 5 devuelve 6
    """

    if numero >= NUMERO_CORTE:
        numero += 1
        return numero
    else:
        raise NumeroError(f"El número {numero} es inferior a {NUMERO_CORTE}")