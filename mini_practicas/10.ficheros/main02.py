with open("fichero-utf8.txt", "w", encoding = "utf-8") as fichero:
    fichero.write("Una línea\n")
    fichero.write("Otra con ñs y ás, és, ís...\n")
    fichero.write("Otra con 😀 ")



print("\n\nLectura del fichero sin encoding:")
print("-" * 30)
with open("fichero-utf8.txt", "r") as fichero:
    print(fichero.read())

print("\n\nLectura del fichero con utf-8:")
print("-" * 30)
with open("fichero-utf8.txt", "r", encoding = "utf-8") as fichero:
    print(fichero.read())

print("\n\nLectura del fichero con iso-8859-1:")
print("-" * 30)
with open("fichero-utf8.txt", "r", encoding = "iso-8859-1") as fichero:
    print(fichero.read())

print("\n\nLectura del fichero con ascii:")
print("-" * 30)
with open("fichero-utf8.txt", "r", encoding = "ascii") as fichero:
    print(fichero.read())
