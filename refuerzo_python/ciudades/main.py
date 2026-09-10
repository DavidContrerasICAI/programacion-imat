if __name__ == "__main__":
    dict_cp = {"Madrid": "28", "Barcelona": "08"}

    personas_limpias = []
    personas = [linea1, linea2, linea3, linea4]

    for persona in personas:
        campos = persona.split(";")
        if len(campos) == 5:
            nombre, edad, direccion, cp, ciudad = persona.split(";")
            edad = int(edad)
            if edad > 0 and edad < 99:
                dict_valor = dict_cp[ciudad.capitalize()]
                if cp.startswith(dict_valor):
                    cp = int(cp)
                    personas_limpias.append((nombre, edad, direccion, cp, ciudad))   
                else:
                    print(f">>> Error #001: el cp {cp} no se corresponde con la ciudad {ciudad} -->", persona)
            else:
                print(">>> Error #982: edad no válida -->", persona)
        else:
            print(">>> Error #435: faltan datos -->", persona)

    print(personas_limpias)