letra = "A"
cadena = "AskAsdAfdsfdsgfgdsgf jgdgfjhdsgfhj gdshfjgdshjfgdshjgfjhdsgfjs"

encontrada = False
i = 0
while i < len(cadena) and not encontrada:
    if letra == cadena[i]:
        encontrada = True
    i += 1
    
if encontrada:
    print(f"La cadena {cadena} contiene la letra {letra}")
else:
    print(f"La cadena NO {cadena} contiene la letra {letra}")

if encontrada:
    valor = "SI"
else:
    valor = "NO"
    
print(f"La cadena {valor} {cadena} contiene la letra {letra}")

letra = "A"
cadena = "AskAsdAfdsfdsgfgdsgf jgdS S A Agfjhdsgfhj gdshfjgdshjfgdshjgfjhdsgfjA"

n = 0
i = 0
while i < len(cadena):
    if letra == cadena[i]:
        n += 1
    i += 1
    
if n > 0:
    print(f"La cadena {cadena} tiene {n} {letra}s")
else:
    print(f"La cadena NO {cadena} tiene la letra {letra}")

print()
print("*"*30)
print()

cadena1 = "abca"   # índice i 
cadena2 = "absbagertayse"    # índice j
i = 0
while i < len(cadena1):
    n = 0
    j = 0
    while j < len(cadena2):
        #print(cadena1[i], cadena2[j])
        if cadena1[i] == cadena2[j]:
            #print("OK")
            n += 1
        j += 1
    print(f"{cadena1[i]}:{n}")
    i += 1

print("?????????????????")
print("?????????????????")
print("?????????????????")
print("?????????????????")

nueva_entrada = "d:10"
s = "a:10,b:5,c:999"

existe = False
valor = ""
i = 0
while i < len(s):
    if s[i] == ",":
        if valor == nueva_entrada:
            existe = True
        valor = ""
    else:
        valor += s[i]
    i += 1

if not existe:
    s += "," + nueva_entrada
print(s)
