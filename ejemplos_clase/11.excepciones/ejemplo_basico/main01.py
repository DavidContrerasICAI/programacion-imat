try:
    edad = input("Edad: ")
    edad_int = int(edad)
    nombre = input("Nombre: ")
    info = nombre, edad_int
    print(info)
    print("Persona creada con éxito")
except ValueError as error:
    print("Error: no se pudo crear la persona. Edad no válida")