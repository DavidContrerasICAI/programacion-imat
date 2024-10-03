opcion_numero = 0

while opcion_numero != 9:

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
    opcion_numero = int(opcion)  
    
    if opcion_numero > 0 and opcion_numero < 5:  # +, -, *, %...   
        """
        Iteración II: el tipo de dato coincida con lo introducido
        """
        tipo_dato = input("Tipo de dato: ")
        while tipo_dato != "int" and tipo_dato != "float" and tipo_dato != "complex":
            print("Tipo de dato no válido")
            tipo_dato = input("Tipo de dato: ")
        
        """
        Iteración III: el tipo de dato coincida con lo introducido
        """
        error_entrada_tipo = True
        while error_entrada_tipo == True:
            numero1_str = input("Número #1: ")
            numero2_str = input("Número #2: ")
            
            if tipo_dato == "int":
                if numero1_str.isdecimal() and numero2_str.isdecimal():
                    numero1 = int(numero1_str)
                    numero2 = int(numero2_str) 
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True
            elif tipo_dato == "float":
                if numero1_str.count(".") == 1 and numero2_str.count(".") == 1:
                    numero1 = float(numero1_str)
                    numero2 = float(numero2_str)
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True
            elif tipo_dato == "complex": 
                if numero1_str.count("+") == 1 and numero1_str.count("j") == 1 \
                        and numero2_str.count("+") == 1 and numero2_str.count("j") == 1:
                    numero1 = complex(numero1_str)
                    numero2 = complex(numero2_str)
                    error_entrada_tipo = False
                else:
                    error_entrada_tipo = True 
            
            if error_entrada_tipo:
                print(f"Error: los números introducidos no son {tipo_dato}")

        if opcion_numero == 1:  #sumar
            resultado = numero1 + numero2
            caracter_operacion = "+"
        elif opcion_numero == 2:  #restar
            resultado = numero1 - numero2
            caracter_operacion = "-"  
        elif opcion_numero == 3:  #multiplicar
            resultado = numero1 * numero2
            caracter_operacion = "*"

        print("---------------------------------------------")
        print(numero1, caracter_operacion, numero2, "=", resultado)     
        print("---------------------------------------------")
    elif opcion_numero == 5:  # abs
        numero1_str = input("Número #1: ") 
        numero1 = int(numero1_str)
        resultado = abs(numero1)
        print("---------------------------------------------")
        print("El valor absoluto de", numero1, "es", resultado)
        print("---------------------------------------------")
    elif opcion_numero == 6:  # Rendondeo de un float
        numero1_str = input("Número decimal: ") 
        numero1 = float(numero1_str)
        resultado = round(numero1)
        print("---------------------------------------------")
        print("El valor redondeado de", numero1, "es", resultado)
        print("---------------------------------------------")
    elif opcion_numero == 7:  # char to ascci
        char = input("Carácter: ") 
        resultado = ord(char)
        print("---------------------------------------------")
        print("El valor ASCII de", char, "es", resultado)
        print("---------------------------------------------")
    elif opcion_numero == 8:  # char to ascci
        numero1_str = input("Valor ASCII: ") 
        numero1 = int(numero1_str)
        resultado = chr(numero1)
        print("---------------------------------------------")
        print("El carácter de valor ASCII", numero1_str, "es", resultado)
        print("---------------------------------------------")
    elif opcion_numero == 9:  # Bye
        print("Bye!")
    else:
        print("Opción no válida")
