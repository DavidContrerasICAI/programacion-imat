f = open("data\\personas_new.txt", "r")
nombre = f.readline()
while nombre != "":
    edad = f.readline()
    print(nombre.strip(), edad.strip())
    nombre = f.readline()
f.close()

print("\n=======\n")
f = open("data\\personas_new.txt", "r")
for nombre in f:    # readline()
    edad = f.readline()
    direccion = f.readline()
    print(nombre.strip(), edad.strip(), direccion.strip())
f.close()

print("\n=======\n")
f = open("personas_chat.txt", "r")    # OJO, no se especifica la codificación, atento al texto "años"
header = f.readline()
_ = f.readline()
for linea in f:
    print(linea.strip())
f.close()

print("\n=======\n")
with open("data\\personas_new.txt", "r") as f:
    for nombre in f:    # readline()
        edad = f.readline()
        direccion = f.readline()
        print(nombre.strip(), edad.strip(), direccion.strip())

print("\n=======\n")
with open("data\\fichero_raro.txt", "r") as f:
    for linea in f:
        print(linea.strip())

print("\n=======\n")
with open("data\\fichero_raro.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())

