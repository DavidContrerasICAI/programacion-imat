# Cuenta cuántas veces aparece una letra dentro de una cadena.
# Recorre toda la cadena con un contador (n) y muestra el número de
# apariciones o un mensaje indicando que la letra no aparece.

letra = "a"
cadena = "Esto es una cadena de ejemplo"

n = 0
i = 0
while i < len(cadena):
    if letra == cadena[i]:
        n += 1
    i += 1
    
if n > 0:
    print(f"La cadena \"{cadena}\" tiene {n} \"{letra}\"")
else:
    print(f"La cadena NO \"{cadena}\" tiene la letra \"{letra}\"")
