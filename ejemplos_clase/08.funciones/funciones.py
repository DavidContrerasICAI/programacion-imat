def identificacion_caracteres_unicos(cadena:str) -> dict:
    """
    Identifica caracteres únicos para poder hacer la cuenta posterior
    Ejemplo:
        "carlacaca" --> "carl"
    """
    frecuencias_dict = {}
    i = 0
    while i < len(cadena):
        # Detectamos caracteres únicos en la cadena para no crear duplicados de frecuencias
        letra = cadena[i]

        if letra not in frecuencias_dict:
            frecuencias_dict[letra] = 1
        else:
            frecuencias_dict[letra] = frecuencias_dict[letra] + 1

        i += 1

    return frecuencias_dict

def ordenar(frecuencias_dict:dict) -> dict:
    frecuencias_sorted = set(frecuencias_dict.values())   # se eliminan los duplicados
    frecuencias_sorted = sorted(frecuencias_sorted, reverse=True)   # se ordenan de forma inversa
    return frecuencias_sorted


def calculo_frecuencias(frecuencias_dict:dict, frecuencias_sorted:dict):
    frecuencias_dict_inv = {}
    for k, v in frecuencias_dict.items():
        if v in frecuencias_dict_inv:
            frecuencias_dict_inv[v].append(k)
        else:
            frecuencias_dict_inv[v] = [k]

    print("Tabla de frecuencia: ", end = "")
    for frecuencia in frecuencias_sorted:
        letras = frecuencias_dict_inv[frecuencia]
        for letra in letras:
            print(f"{letra}:{frecuencia},", end = "")

