cadena = "Hola soy Manuel"
nueva_cadena = ""


# Opción 1
i = 0
while i < len(cadena):
    if cadena[i] != " ":
        #nueva_cadena = nueva_cadena + cadena[i] 
        nueva_cadena += cadena[i] 
    i += 1

print(nueva_cadena)

# Opción 2
nueva_cadena = nueva_cadena.replace(" ", "")
print(nueva_cadena)

# Opción 3
nueva_cadena = ""
print("CON FOR")
print("="*10)
for caracter in cadena:
    if caracter != " ":
        nueva_cadena += caracter

print(nueva_cadena)

cadena = "Luis"
letra = "u"
if letra in cadena:
    print(f"{cadena} contiene \"{letra}\"")