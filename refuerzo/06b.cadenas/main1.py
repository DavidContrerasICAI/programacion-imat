# Busca si una letra concreta está dentro de una cadena.
# Recorre la cadena carácter a carácter con un bucle while y una bandera
# (encontrada) y muestra por pantalla "SI" o "NO" junto con un mensaje.

letra = "a"
cadena = "Esto es una cadena de ejemplo"

encontrada = False
i = 0
while i < len(cadena) and not encontrada:
    if letra == cadena[i]:
        encontrada = True
    i += 1

if encontrada:
    valor = "SI"
else:
    valor = "NO"
    
print(f"La cadena \"{cadena}\" {valor} contiene la letra \"{letra}\"")
