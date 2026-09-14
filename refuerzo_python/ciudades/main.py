import re
from constantes import NUMERO_CAMPOS, EDAD_MAX, EDAD_MIN, dict_cp

if __name__ == "__main__":
    patron = r"^(?:Calle|Avenida)\s+.+,\s*\d+$"

    personas_limpias = []
    personas = []

    contador_error = 0

    fichero = open("data/personas.txt", "r", encoding="UTF-8")
    for linea in fichero:
        linea = linea.strip()
        campos = linea.split(";")
        funciones.validar()

    fichero.close()
    print(f"Se procesaron {len(personas_limpias)} personas correctamente y {contador_error} con errores")
    print(personas_limpias)

    