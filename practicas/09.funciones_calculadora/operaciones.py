import salida 

def sumar(numero1:int|float|complex, numero2:int|float|complex) -> str:
    """
    Realiza la operación SUMAR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """
    resultado = numero1 + numero2
    caracter_operacion = "+"
    salida = f"{numero1} {caracter_operacion} {numero2} = {resultado}"
    return salida

def restar(numero1:int|float|complex, numero2:int|float|complex) -> str:
    """
    Realiza la operación RESTAR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """

    resultado = numero1 - numero2
    caracter_operacion = "-" 
    salida = f"{numero1} {caracter_operacion} {numero2} = {resultado}"
    return salida
    
def multiplicar(numero1:int|float|complex, numero2:int|float|complex) -> str:
    """
    Realiza la operación MULTIPLICAR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """
    resultado = numero1 * numero2
    caracter_operacion = "*" 
    salida = f"{numero1} {caracter_operacion} {numero2} = {resultado}"
    return salida
    
def dividir(numero1:int|float|complex, numero2:int|float|complex) -> str:
    """
    Realiza la operación DIVIDIR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """

    resultado = numero1 / numero2
    caracter_operacion = "/" 
    salida = f"{numero1} {caracter_operacion} {numero2} = {resultado}"
    return salida
    
def calcular_abs() -> str:
    """
    Lee el número, realiza la operación ABS y muestra su resultado 
    """
    numero1_str = input("Número: ") 
    numero1 = int(numero1_str)
    resultado = abs(numero1)
    salida = f"El valor absoluto de {numero1} es {resultado}"
    return salida

def calcular_round() -> str:
    """
    Lee el número, realiza la operación ROUND y muestra su resultado 
    """
    numero1_str = input("Número decimal: ") 
    numero1 = float(numero1_str)
    resultado = round(numero1)
    salida = f"El valor redondeado de {numero1} es {resultado}"
    return salida
    
def calcular_ascii() -> str:
    """
    Lee el número, realiza la operación ASCII y muestra su resultado 
    """
    char = input("Carácter: ") 
    resultado = ord(char)
    salida = f"El valor ASCII de {char} es {resultado}"
    return salida
    
def calcular_caracter() -> str:
    """
    Lee el número, realiza la operación CHAR y muestra su resultado 
    """
    numero_str = input("Valor ASCII: ") 
    numero = int(numero_str)
    resultado = chr(numero)
    salida = f"El carácter de valor ASCII {numero} es {resultado}"
    return salida
