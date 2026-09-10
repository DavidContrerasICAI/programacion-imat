if __name__ == "__main__":
    dict_cp = {
    "Madrid": "28",
    "Barcelona": "43",
    "Valencia": "58",
    "Sevilla": "19",
    "Málaga": "76",
    "Zaragoza": "32",
    "Bilbao": "61",
    "Oviedo": "45",
    "Gijón": "45",
    "Murcia": "20",
    "Las Palmas de Gran Canaria": "83",
    "Santa Cruz de Tenerife": "17",
    "Pamplona": "69",
    "Logroño": "28",
    "Salamanca": "52",
    "Valladolid": "94",
    "León": "31",
    "A Coruña": "78",
    "Vigo": "16",
    "Alicante": "60",
    "Granada": "42",
    "Córdoba": "85",
    "Albacete": "27",
    "Ciudad Real": "73",
    "Guadalajara": "51",
    "Cuenca": "38",
    "Toledo": "92",
    "Cáceres": "24",
    "Badajoz": "71",
    "Segovia": "49",
    "Ávila": "86",
    "Palencia": "13",
    "Soria": "60",
    "Burgos": "35",
    }

    personas_limpias = []
    personas = []

    fichero = open("data/personas.txt", "r", encoding="UTF-8")
    for linea in fichero:
        campos = linea.split(";")
        if len(campos) == 5:
            nombre, edad, direccion, cp, ciudad = linea.split(";")
            edad = int(edad)
            ciudad = ciudad.strip()
            if edad > 0 and edad < 99:
                dict_valor = dict_cp[ciudad]
                if cp.startswith(dict_valor):
                    cp = int(cp)
                    personas_limpias.append((nombre, edad, direccion, cp, ciudad))   
                else:
                    print(f">>> Error #001: el cp {cp} no se corresponde con la ciudad {ciudad} -->", linea)
            else:
                print(">>> Error #982: edad no válida -->", linea)
        else:
            print(">>> Error #435: faltan datos -->", linea)

    fichero.close()

    print(personas_limpias)
    