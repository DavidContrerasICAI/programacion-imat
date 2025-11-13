def crear_diccionario_reemplazos(tipo:str="fijo")->dict:
    if tipo.lower() == "fijo":
        dict_reemplazos = {"-": "", "+": "", "á":"a", "é":"e", "í": "i", "ó": "o", "ú": "u"}
    else:
        dict_reemplazos = {}
        fichero = open("data/reemplazos.txt", "r", encoding="utf-8")
        for linea in fichero:
            caracteres = linea.strip().split(":")
            buscar, reemplazar = caracteres
            if len(caracteres) == 1:
                reemplazar = ""
            dict_reemplazos[buscar] = reemplazar
    return dict_reemplazos

def crear_diccionario_ropa(dict_reemplazos:dict)->dict:
    dict_ropas = {}
    fichero = open("data/ropa.csv", "r", encoding="utf-8") 
    _ = fichero.readline()
    #linea_encabezado = fichero.readline()
    for linea in fichero:
        linea = linea.strip()
        lista_prendas = linea.split(",")
        if len(lista_prendas) == 3:
            ropa, precio, temporada = lista_prendas
            precio = float(precio.strip())
            ropa = ropa.strip()
            temporada = temporada.strip()
            for k, v in dict_reemplazos.items():
                ropa = ropa.replace(k, v)
            dict_ropas[ropa] = (precio, temporada)
    return dict_ropas

def listar_ropa(dict_reemplazos:dict)->None:
    for ropa, valor in dict_reemplazos.items():
        precio, temporada = valor 
        print(f"{ropa}: {precio}€ - Temporada: {temporada}")