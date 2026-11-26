numero_correcto = False
while not numero_correcto:
    try:
        edad = int(input("Edad: "))
        numero_correcto = True
    except:
        print("Debes introducir un número como edad")
