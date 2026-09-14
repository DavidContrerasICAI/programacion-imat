import funciones as f

if __name__ == "__main__":
    personas_limpias = []
    contador_error = 0

    fichero = open("data/personas.txt", "r", encoding="UTF-8")
    for linea in fichero:
        linea = linea.strip()
        if not f.validar_linea_persona(personas_limpias, linea):
            contador_error += 1

    fichero.close()
    print(f"Se procesaron {len(personas_limpias)} personas correctamente y {contador_error} con errores")
    print(personas_limpias)

    