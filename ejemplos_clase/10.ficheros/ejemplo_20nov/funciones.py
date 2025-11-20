def leer_coches()->dict:
    fichero_error = open("errores.txt", "w", encoding="utf-8")
    diccionario_coches = {}
    for i in range(1, 4):
        nombre_fichero = f"coches{i}.txt"
        fichero = open(nombre_fichero, "r", encoding="utf-8")

        numero_linea_error = 1
        _ = fichero.readline()
        for linea in fichero:
            numero_linea_error += 1
            linea = linea.strip()
            coche, cv_str = linea.split("#")
            cv = transformar_cv(cv_str)
            if cv != -1:
                diccionario_coches[coche] = cv
            else:
                fichero_error.write(f"{numero_linea_error}: {linea}\n")
                
        fichero.close()

    fichero_error.close()
    return diccionario_coches

def transformar_cv(cv_str:str)->int:
    """
    Transforma y filtra los caballos del coche
    de una forma pocoo eficiente y no estructurada
    NO EXCEPCIONES - NO EFICIENTE - SUCIO
    ------ MALA PRÁCTICA -------
    """
    if len(cv_str) < 4:
        try:
            cv = int(cv_str)
            if cv > 100:
                return cv
            else:
                return -1
        except:
            return -1
    else:
        return -1
    