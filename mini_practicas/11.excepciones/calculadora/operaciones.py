import salida 

def sumar(numero1, numero2):
    """
    Realiza la operación SUMAR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """
    resultado = numero1 + numero2
    caracter_operacion = "+"
    salida.generar_salida(numero1, numero2, caracter_operacion, resultado)

def restar(numero1, numero2):
    """
    Realiza la operación RESTAR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """

    resultado = numero1 - numero2
    caracter_operacion = "-" 
    salida.generar_salida(numero1, numero2, caracter_operacion, resultado)
    
def multiplicar(numero1, numero2):
    """
    Realiza la operación MULTIPLICAR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """
    resultado = numero1 * numero2
    caracter_operacion = "*" 
    salida.generar_salida(numero1, numero2, caracter_operacion, resultado)
    
def dividir(numero1, numero2):
    """
    Realiza la operación DIVIDIR y muestra su resultado 
    
    Args:
        numero1 (int/float/complex): primer número sobre el que realizar la operación
        numero2 (int/float/complex): segundo número sobre el que realizar la operación
    """

    resultado = numero1 / numero2
    caracter_operacion = "/" 
    salida.generar_salida(numero1, numero2, caracter_operacion, resultado)
    
def calcular_abs():
    """
    Lee el número, realiza la operación ABS y muestra su resultado 
    """
    numero1_str = input("Número: ") 
    numero1 = int(numero1_str)
    resultado = abs(numero1)
    salida.generar_salida_unaria("El valor absoluto de", numero1, "abs", resultado)

def calcular_round():
    """
    Lee el número, realiza la operación ROUND y muestra su resultado 
    """
    numero1_str = input("Número decimal: ") 
    numero1 = float(numero1_str)
    resultado = round(numero1)
    salida.generar_salida_unaria("El valor redondeado de", numero1, "round", resultado)
    
def calcular_ascii():
    """
    Lee el número, realiza la operación ASCII y muestra su resultado 
    """
    char = input("Carácter: ") 
    resultado = ord(char)
    salida.generar_salida_unaria("El valor ASCII de", char, "ord", resultado)
    
def calcular_caracter():
    """
    Lee el número, realiza la operación CHAR y muestra su resultado 
    """
    numero_str = input("Valor ASCII: ") 
    numero = int(numero_str)
    resultado = chr(numero)
    salida.generar_salida_unaria("El carácter de valor ASCII", numero, "chr", resultado)
