# Igual que main3.py pero sin repetir frecuencias.
# Antes de añadir una frecuencia comprueba, recorriendo la cadena de
# resultados, si ese "carácter:frecuencia" ya existe; al final elimina la
# última coma sobrante.

cadena1 = "abca"            # índice i 
cadena2 = "absbagertayse"   # índice j

frecuencias = ""

i = 0
while i < len(cadena1):
    n = 0
    j = 0
    while j < len(cadena2):
        if cadena1[i] == cadena2[j]:
            n += 1
        j += 1
    nueva_frecuencia = f"{cadena1[i]}:{n}"

    frecuencia = ""
    existe = False
    j = 0
    while j < len(frecuencias):
        if frecuencias[j] == ",":
            if frecuencia == nueva_frecuencia:
                existe = True
                frecuencia = ""
        else:
            frecuencia += frecuencias[j]
        j += 1

    if not existe:
        frecuencias += nueva_frecuencia + ","

    i += 1

frecuencias = frecuencias[:-1]
print(frecuencias)
