"""
Solución al examen inter con LISTAS y TUPLAS
Author: David Contreras
Date: 2/nov
Changed: 2/nov
Version: 3.11 
"""


cadena = "adcdabbdbcdbdc"
cadena = "abbccc"

caracteres_unicos = []
frecuencias = []

print("Cadena de entrada:", cadena)

i = 0
while i < len(cadena):
    # Detectamos caracteres únicos en la cadena para no crear duplicados de frecuencias
    letra = cadena[i]

    if letra not in caracteres_unicos:
        caracteres_unicos.append(letra)

        cuenta = cadena.count(letra)

        # Ordenación de las frecuencias
        k = 0
        pos_final = 0
        while k < len(frecuencias):
            dato = frecuencias[k]   # dato => ("a", 3) (tuple)
            num1 = dato[1]  # num1 => 3 (int)
            if cuenta > num1:
                pos_final = k
                k = len(frecuencias)
            else:
                k += 1
                pos_final = k

        tupla = (letra, cuenta)
        frecuencias.insert(pos_final, (letra, cuenta))

    i += 1

print("Tabla de frecuencia:", frecuencias)

for tupla in frecuencias:
    print(f"\"{tupla[0]}\": {tupla[1]}, ", end = "")