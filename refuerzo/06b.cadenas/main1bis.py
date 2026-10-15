# Igual que main1.py pero sin usar un flag (booleano).
# Avanza el índice i mientras no encuentre la letra; al terminar, si i llegó
# al final de la cadena significa que la letra no estaba.

letra = "a"
cadena = "Esto es una cadena de ejemplo"

encontrada = False
i = 0
while i < len(cadena) and letra != cadena[i]:
    i += 1

if i == len(cadena):
    valor = "no"
else:
    valor = "sí"
    
print(f"La cadena \"{cadena}\" {valor} contiene la letra \"{letra}\"")
