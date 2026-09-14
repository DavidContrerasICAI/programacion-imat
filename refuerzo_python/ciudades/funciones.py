def validar():        
    if len(campos) == NUMERO_CAMPOS:
        nombre, edad, direccion, cp, ciudad = linea.split(";")
        edad = int(edad)
        ciudad = ciudad.strip()
        if edad >= EDAD_MIN and edad < EDAD_MAX:
            dict_valor = dict_cp[ciudad]
            if cp.startswith(dict_valor):
                cp = int(cp)
                if re.match(patron, direccion, re.IGNORECASE):
                    personas_limpias.append((nombre, edad, direccion, cp, ciudad))   
                else:
                    contador_error += 1
                    print(f">>> Error #8899: dirección no es correcta: ", direccion)
            else:
                contador_error += 1
                print(f">>> Error #001: el cp {cp} no se corresponde con la ciudad {ciudad} -->", linea)
        else:
            contador_error += 1
            print(">>> Error #982: edad no válida -->", linea)
    else:
        contador_error += 1
        print(">>> Error #435: faltan datos -->", linea)