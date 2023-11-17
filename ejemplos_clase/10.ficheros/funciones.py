def mostrar_menu() -> int:
    print("Gestión de Personas")
    print("===================")
    print("1. Crear fichero con valores por defecto")
    print("2. Leer personas del fichero")
    print("3. Guardar personas en el fichero")
    print("4. Modificar una edad")
    print("5. Mostrar diccionario de personas")
    print("9. Salir")

    opc = int(input("Operacion > "))

    return opc

def crear_fichero_personas() -> None:
    file = open("personas.txt", "w")
    file.write("nombre, edad\n")
    file.write("Ana, 12\n")
    file.write("Luis, 22\n")
    file.write("Maria, 32\n")
    file.write("Jaime, 26\n")
    file.close()


def escribir_personas(personas:dict) -> None:
    file = open("personas.txt", "w")
    file.write("nombre, edad\n")
    for nombre, edad in personas.items():
        file.write(f"{nombre}, {edad}\n")

    file.close()

def leer_personas() -> dict:
    file = open("personas.txt", "r")
    personas = {}

    encabezado_que_no_me_interesa = file.readline()
    for linea in file:
        campos = linea.split(",")
        nombre = campos[0].strip()
        edad = int(campos[1].strip())
        personas[nombre] = edad

    file.close()
    return personas