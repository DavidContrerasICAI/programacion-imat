import os

historial_operaciones = dict()

def mostrar_menu():
    """
    Muestra el menu principal de la Calculadora
    """
    print("******** Calculadora iMAT ********")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print(" ")
    print("5. Valor absoluto")
    print("6. Redondeo de un número al alza")
    print("7. Valor ASCII de un carácter")
    print("8. Carácter de un código ASCII")
    print("")
    print("9. Salir")
    print("10. Historial de operaciones")
    print("11. Repetir operación")
    print("**********************************")


def leer_tipo_dato():
    """
    Lee y valida el tipo de dato con el cual se va a trabajar
    
    Returns:
        tipo_dato (str): tipo de dato con los valores int, float o complex
    """
    tipo_dato = input("Tipo de dato: ")
    while tipo_dato != "int" and tipo_dato != "float" and tipo_dato != "complex":
        print("Tipo de dato no válido")
        tipo_dato = input("Tipo de dato: ")
        
    return tipo_dato
    
def validar_tipo_dato(tipo_dato, ordinal):
    """
    Lee y valida el número introducido. Debe coincidir con el tipo de dato definido previamente.
    
    Args:
        tipo_dato (str): tipo de dato introducido previamente
        ordinal (int): ordinal del dato: 1º o 2º
        
    Returns:
        numero (int/float/complex): número 
    """
    numero = 0
    error_entrada_tipo = True
    while error_entrada_tipo == True:
        numero_str = input(f"Número #{ordinal}: ")
        if tipo_dato == "int":
            if numero_str.isdecimal():
                numero = int(numero_str)
                error_entrada_tipo = False
            else:
                error_entrada_tipo = True
        elif tipo_dato == "float":
            if numero_str.count(".") == 1:
                numero = float(numero_str)
                error_entrada_tipo = False
            else:
                error_entrada_tipo = True
        elif tipo_dato == "complex": 
            if numero_str.count("+") == 1 and numero_str.count("j") == 1:
                numero = complex(numero_str)
                error_entrada_tipo = False
            else:
                error_entrada_tipo = True 

        if error_entrada_tipo:
            print(f">>>Error: el número introducido no es {tipo_dato}")

    return numero


def generar_salida_unaria(mensaje, operando, operacion, resultado):
    """
    Genera la salida por pantalla como resultado de las operaciones unarias
        y almacena la operación en el diccionario de histórico
    
    Args:
        mensaje (str): mensaje variable a mostrar
        operando (int/float/complex): valor de la operación
        operacion (str): operación a realizar. abs, round, ...
        resultado (int/float/complex): resultado de la operación
    """
    global historial_operaciones  # No es necesario, pero nos ayuda a entender el concepto
    os.system("cls")
    print("---------------------------------------------")
    salida = f"{mensaje} {operando} es {resultado}"
    print(salida)
    clave = len(historial_operaciones) + 1
    historial_operaciones[clave] = (operando, operacion, resultado) 
    print("---------------------------------------------")
    print("")
    
def generar_salida(numero1, numero2, caracter_operacion, resultado):
    """
    Genera la salida por pantalla como resultado de las operaciones binarias
        y almacena la operación en el diccionario de histórico
    
    Args:
        numero1 (int/float/complex): operador 1
        numero2 (int/float/complex): operador 2
        operacion (str): operación a realizar. +, -, ...
        resultado (int/float/complex): resultado de la operación
    """
    global historial_operaciones  # No es necesario, pero nos ayuda a entender el concepto
    os.system("cls")
    print("---------------------------------------------")
    salida = f"{numero1} {caracter_operacion} {numero2} = {resultado}"
    print(salida)  
    clave = len(historial_operaciones) + 1
    historial_operaciones[clave] = (numero1, caracter_operacion, numero2, resultado)
    print("---------------------------------------------")
    print("")
    
def mostrar_historial(): 
    global historial_operaciones  # No es necesario, pero nos ayuda a entender el concepto
    os.system("cls")
    print(f"{'Historial':^20}")
    print("=" * 20)
    for clave, operacion in historial_operaciones.items():
        print(f"· {clave}: INPUT: {operacion[:-1]} -> OUTPUT: {operacion[-1:][0]}")
    print("")
        
def repetir_operacion():
    global historial_operaciones  # No es necesario, pero nos ayuda a entender el concepto
    clave_str = input("Clave de la operación: ")
    clave = int(clave_str)
    operacion = historial_operaciones[clave]
    salida = ""
    for i in range(0, len(operacion)):
        if i == len(operacion)-1:
            salida += " ="
        salida += " " + str(operacion[i])
    
    os.system("cls")
    print(f"Operación {clave}: {salida}")
    print("")