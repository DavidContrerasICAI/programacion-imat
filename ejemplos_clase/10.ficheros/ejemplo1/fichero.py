def escribir() -> None:
    fichero = open("datos.txt", "w")
    
    fichero.write("Luis\n")
    fichero.write("22\n")
    fichero.write("Ana\n")
    fichero.write("33\n")
    fichero.write("María\n")
    fichero.write("20\n")

    fichero.close()     

def leer_primera_persona() -> tuple[str, int]:
    fichero = open("datos.txt", "r")
    nombre = fichero.readline()
    nombre = nombre.rstrip()
    edad_str = fichero.readline()
    edad_str = edad_str.rstrip()
    edad = int(edad_str)
    
    return nombre, edad

def leer_personas() -> list[tuple[str, int]]:
    personas = []
    fichero = open("datos.txt", "r") 
    nombre = fichero.readline()    # do - while
    while nombre != "":
        nombre = nombre.rstrip()
        edad_str = fichero.readline()
        edad_str = edad_str.rstrip()
        edad = int(edad_str)
        personas.append((nombre, edad))
        nombre = fichero.readline()    # do - while

    return personas

def leer_personas_for() -> list[tuple[str, int]]:
    personas = []
    fichero = open("datos.txt", "r") 
    for nombre in fichero:    # Implícitamente se hace un readline()
        nombre = nombre.rstrip()
        edad_str = fichero.readline()    # se lee una línea más
        edad_str = edad_str.rstrip()
        edad = int(edad_str)
        personas.append((nombre, edad))
    
    fichero.close()
    return personas




