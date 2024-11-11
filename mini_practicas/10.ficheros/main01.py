print("\n\nLectura del fichero sin enconding:")
print("-" * 30)
with open("a.txt", "r") as fichero:
    print(fichero.read())

print("\n\nLectura del fichero con cp1252:")
print("-" * 30)
with open("a.txt", "r", encoding = "cp1252") as fichero:
    print(fichero.read())

print("\n\nLectura del fichero con utf-8:")
print("-" * 30)
with open("a.txt", "r", encoding = "utf-8") as fichero:
    print(fichero.read())


