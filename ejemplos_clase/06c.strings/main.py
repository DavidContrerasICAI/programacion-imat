cadena = "hola"
print(type(cadena))

print(cadena.upper())    # Métodos de str
print(cadena.lower())    # Métodos de str

i = 8
#i.upper()   # error

numero_int = int("22")

print(len(cadena))    # Funcion len()

ciudad = "maDriD"

print(ciudad.capitalize())

ciudad_cap = ciudad[0].upper() + ciudad[1:].lower()

pos = ciudad.index("a")    # --> 1
es_digito = ciudad.isdigit()
# ciudad_cap[0] = "X"   # ERROR, una cadena es inmutable
ciudad_cap = ciudad_cap.replace("d", "X")
print(ciudad_cap)