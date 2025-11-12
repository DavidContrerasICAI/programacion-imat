fichero = open("ropa.txt", "r", encoding="utf-8") 
ropas = []
for linea in fichero:
    linea = linea.strip()
    ropas.append(linea)
    print(linea)

print(ropas)
