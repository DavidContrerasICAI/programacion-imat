import os

def mostrar_menu() -> None:
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

def generar_salida(historial_operaciones:dict, operacion:str) -> None:
    """
    Genera la salida por pantalla como resultado de las operaciones binarias
        y almacena la operación en el diccionario de histórico
    
    Args:
        numero1 (int|float|complex): operador 1
        numero2 (int|float|complex): operador 2
        operacion (str): operación a realizar. +, -, ...
        resultado (int|float|complex): resultado de la operación
    """
    os.system("cls")
    print("---------------------------------------------")
    print(operacion)  
    print("---------------------------------------------")
    clave = len(historial_operaciones) + 1
    historial_operaciones[clave] = operacion
    print("")
    
def mostrar_historial(historial_operaciones:dict) -> None:
    os.system("cls")
    print(f"{'Historial':^20}")
    print("=" * 20)
    for clave, operacion in historial_operaciones.items():
        print(f"· {clave}: {operacion}")
    print("")
        
def repetir_operacion(historial_operaciones:dict) -> None:
    clave_str = input("Clave de la operación: ")
    clave = int(clave_str)
    operacion = historial_operaciones[clave]
    os.system("cls")
    print(f"Operación {clave}: {operacion}")
    print("")