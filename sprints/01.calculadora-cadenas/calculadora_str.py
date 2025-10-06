"""
SOLUCIÓN COMPLETA CON STRINGS
Y CON TODAS LAS ITERACIONES
"""

opcion_entera = 0

while opcion_entera != 9:

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
    print("**********************************")

    opcion = input("Operación: ")
    opcion_entera = int(opcion)  
    
    if opcion_entera < 5:  # +, -, *, %...   
        if opcion_entera <= 0:    # De momento no sabemos trabajar con operaciones lógicas. Este código se mejorará en el futuro. 
            print("Opción no válida")
        else:
            tipo_dato = input("Tipo de dato: ")
            tipo_dato_no_valido = True

            """
            Iteración II: el tipo de dato coincida con lo introducido
            """
            while tipo_dato_no_valido:
                tipo_dato_no_valido = False
                if tipo_dato != "int":
                    if tipo_dato != "float":
                        if tipo_dato != "complex":
                            print("Tipo de dato no válido")
                            tipo_dato = input("Tipo de dato: ")
                            tipo_dato_no_valido = True
            
            """
            Iteración III: el tipo de dato coincida con lo introducido
            """
            error_entrada_tipo = True
            
            while error_entrada_tipo:
                error_entrada_tipo = False
                numero1_str = input("Número #1: ")
                numero2_str = input("Número #2: ")
                
                if tipo_dato == "int":
                    if numero1_str.isdecimal():
                        numero1 = int(numero1_str)
                    else:
                        error_entrada_tipo = True
                        print("El número 1 no es un entero")
    
                    if numero2_str.isdecimal():
                        numero2 = int(numero2_str)
                    else:
                        error_entrada_tipo = True
                        print("El número 2 no es un entero")
                else: 
                    if tipo_dato == "float":
                        if numero1_str.count(".") == 1:
                            numero1 = float(numero1_str)
                        else:
                            error_entrada_tipo = True                        
                            print("El número 1 no es un decimal")
                        if numero2_str.count(".") == 1:
                            numero2 = float(numero2_str)
                        else:
                            error_entrada_tipo = True                        
                            print("El número 2 no es un decimal")
                    else: 
                        if tipo_dato == "complex":
                            if numero1_str.count("+") == 1:
                                if numero1_str.count("j") == 1:
                                    numero1 = complex(numero1_str)
                                else:
                                    error_entrada_tipo = True
                                    print("El número 1 no es un complejo")
                                    
                            if numero2_str.count("+") == 1:
                                if numero2_str.count("j") == 1:
                                    numero2 = complex(numero2_str)
                                else:
                                    error_entrada_tipo = True
                                    print("El número 2 no es un complejo")                                

            if opcion_entera == 1:  #sumar
                resultado = numero1 + numero2
                caracter_operacion = "+"
            else:
                if opcion_entera == 2:  #restar
                    resultado = numero1 - numero2
                    caracter_operacion = "-"  
                else:
                    if opcion_entera == 3:  #multiplicar
                        resultado = numero1 * numero2
                        caracter_operacion = "*"

            print("---------------------------------------------")
            print(numero1, caracter_operacion, numero2, "=", resultado)     
            print("---------------------------------------------")
    else:  
        if opcion_entera == 5:  # abs
            numero1_str = input("Número #1: ") 
            numero1 = int(numero1_str)
            resultado = abs(numero1)
            print("---------------------------------------------")
            print("El valor absoluto de", numero1, "es", resultado)
            print("---------------------------------------------")
            
            # NO: print("El valor absoluto de," numero1_str, "es", abs(int(numero1_str)))
        else:
            if opcion_entera == 6:  # Rendondeo de un float
                numero1_str = input("Número decimal: ") 
                numero1 = float(numero1_str)
                resultado = round(numero1)
                print("---------------------------------------------")
                print("El valor redondeado de", numero1, "es", resultado)
                print("---------------------------------------------")
            else:
                if opcion_entera == 7:  # char to ascci
                    char = input("Carácter: ") 
                    resultado = ord(char)
                    print("---------------------------------------------")
                    print("El valor ASCII de", char, "es", resultado)
                    print("---------------------------------------------")
                else:
                    if opcion_entera == 8:  # char to ascci
                        numero1_str = input("Valor ASCII: ") 
                        numero1 = int(numero1_str)
                        resultado = chr(numero1)
                        print("---------------------------------------------")
                        print("El carácter de valor ASCII", numero1_str, "es", resultado)
                        print("---------------------------------------------")
                    else:  # Iteración II
                        if opcion_entera > 9:
                            print("Opción no válida")

                
            