def escribir_fichero_texto():
    file = open("personas.txt", "w")
    file.write("Ana, 12\n")
    file.write("Luis, 22\n")
    file.write("Maria, 32\n")
    file.write("Jaime, 26\n")
    file.close()


def actualizar_personas():
    file = open("personas.txt", "w")
    file.write("Ana, 12\n")
    file.write("Luis, 22\n")
    file.write("Maria, 32\n")
    file.write("Jaime, 26\n")
    file.close()

def leer_fichero_texto() -> dict:
    file = open("personas.txt", "r")
    personas = {}
    for linea in file:
        campos = linea.split(",")
        nombre = campos[0].strip()
        edad = int(campos[1].strip())
        personas[nombre] = edad

    file.close()
    return personas