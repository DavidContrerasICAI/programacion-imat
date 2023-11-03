"""
Solución al examen inter con DICCIONARIOS
Author: David Contreras
Date: 2/nov
Changed: 2/nov
Version: 3.11 
"""


cadena = "adcdabbdbcdbdc"
cadena = "carlacaca"

# caracteres_unicos = []
# frecuencias = []

frecuencias_dict = {}
print("Cadena de entrada:", cadena)

i = 0
while i < len(cadena):
    # Detectamos caracteres únicos en la cadena para no crear duplicados de frecuencias
    letra = cadena[i]

    if letra not in frecuencias_dict:
        frecuencias_dict[letra] = 1
    else:
        frecuencias_dict[letra] = frecuencias_dict[letra] + 1

    i += 1

frecuencias_sorted = set(frecuencias_dict.values())   # se eliminan los duplicados
frecuencias_sorted = sorted(frecuencias_sorted, reverse=True)   # se ordenan de forma inversa

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
