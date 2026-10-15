# Calcula la frecuencia de cada carácter de cadena1 dentro de cadena2.
# Para cada carácter de cadena1 cuenta cuántas veces aparece en cadena2 y
# construye una cadena con el formato "carácter:frecuencia" (repitiendo los
# caracteres que aparecen más de una vez en cadena1).

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
    frecuencias += nueva_frecuencia
    i += 1

print(frecuencias)