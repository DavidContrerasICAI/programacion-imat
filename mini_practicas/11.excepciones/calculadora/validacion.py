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

        if error_entrada_tipo > 0:
            print(f">>>Error: el número introducido no es {tipo_dato}")

    return numero