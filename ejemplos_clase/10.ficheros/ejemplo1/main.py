import fichero as f

if __name__ == "__main__":
    print("1.- Escribir fichero")
    print("2.- Leer la primera persona")
    print("3.- Leer todas las personas")
    print("4.- Leer todas las personas con for")
    opcion_str = input("¿Qué deseas hacer? ")
    opcion = int(opcion_str)
    
    if opcion == 1:
        f.escribir()
    elif opcion == 2:
        persona = f.leer_primera_persona()
        print(persona)
    elif opcion == 3:
        personas = f.leer_personas()
        print(personas)
    elif opcion == 4:
        personas = f.leer_personas_for()
        print(personas)
    