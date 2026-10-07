s = "Hola esto es una pruebaX"
LETRA = "X"
encontrado = False

i = 0
while i < len(s) and not encontrado:
    if s[i] == LETRA:
        encontrado = True
    i += 1

if encontrado:
    print(f"La cadena tiene al menos una {LETRA}")
else:
    print(f"La cadena no tiene ninguna {LETRA}")