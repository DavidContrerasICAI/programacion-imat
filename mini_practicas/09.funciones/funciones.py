"""
Implementa la función split() para que acepte dos
tipos de separadores.

Ejemplo:
cadena = "Hola, esto es uno, dos y tres ejemplos"
lista = splitear(cadena, ",", " ")
lista -> ["Hola", "esto", "es", "uno", "dos", "y", "tres", "ejemplos"]

cadena = "1,2-3,4-5"
lista = splitear(cadena, ",", "-")
lista -> ["1", "2", "3", "4", "5"]

El método split() de str devuelve:
>>> cadena.split()                                                                                                                          
['Hola,', 'esto', 'es', 'uno,', 'dos', 'y', 'tres', 'ejemplos']   
"""

def splitear_chatgpt(cadena, separador1, separador2):
    if not separador1 or not separador2:
        return resultado

    resultado = []
    palabra = ""
    i = 0

    while i < len(cadena):
        if cadena[i:i + len(separador1)] == separador1:
            salto = len(separador1)
        elif cadena[i:i + len(separador2)] == separador2:
            salto = len(separador2)
        else:
            palabra += cadena[i]
            i += 1
            continue

        if palabra:
            resultado.append(palabra)
            palabra = ""

        i += salto

    if palabra:
        resultado.append(palabra)

    return resultado

def splitear(cadena, separador1, separador2):
    """
    Los separadores son de 1 caracter de longitud
    """
    resultado = []
    palabra = ""

    i = 0
    while i < len(cadena):
        if cadena[i] == separador1 or cadena[i] == separador2:
            if len(palabra) > 0:
                resultado.append(palabra)
            palabra = ""
        else:
            palabra += cadena[i]
        i += 1

    resultado.append(palabra)
    return resultado

# Llama aquí a la función splitear
cadena = "Hola, esto es uno, dos y tres ejemplos"
lista_resultado = splitear(cadena, ",", " ")
print(lista_resultado)

cadena2 = "1,2-3,4-5"
lista_resultado = splitear(cadena2, ",", "-")
print(lista_resultado)

"""
Implementa la función find() para que acepte dos
tipos de separadores.

Ejemplo:
cadena = "Hola, esto es uno, dos y tres ejemplos"
lista = findear(cadena, "o")
lista -> [1, 9, 16, 20, 36]
lista = findear(cadena, "x")
lista -> []

El método find() de str devuelve:
>>> cadena.find("o")                                                                                                                        
1    
"""

def findear_chatgpt(cadena, buscado):
    posiciones = []

    if not buscado:
        return posiciones

    for i in range(len(cadena) - len(buscado) + 1):
        if cadena[i:i + len(buscado)] == buscado:
            posiciones.append(i)

    return posiciones

def findear(cadena, buscado):
    """
    Encuentra un caracter
    """
    posiciones = []

    i = 0
    while i < len(cadena):
        if cadena[i] == buscado:
            posiciones.append(i)
        i += 1

    return posiciones
    

# Llama aquí a la función findear

cadena = "Hola, esto es uno, dos y tres ejemplos"
lista_resultado = findear(cadena, "o")
print(lista_resultado)
lista_resultado = findear(cadena, "X")
print(lista_resultado)