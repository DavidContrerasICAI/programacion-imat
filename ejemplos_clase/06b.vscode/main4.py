s = "Hola esto es una pruebaX"
LETRA = "X"

i = 0
while i < len(s) and s[i] != LETRA:
    i += 1

if i == len(s):     # He llegado al final de la cadena
    print(f"La cadena no tiene ninguna {LETRA}")
else:
    print(f"La cadena tiene al menos una {LETRA}")