import funciones as func

if __name__ == "__main__":
    personas = {}

    opc = func.mostrar_menu()
    while opc != 9:
        if opc == 1:
            func.crear_fichero_personas() 
        elif opc == 2:
            personas = func.leer_personas()
        elif opc == 3:
            func.escribir_personas(personas)
        elif opc == 4:
            nombre = input("Persona a cambiar la edad: ")
            if nombre in personas:
                edad = int(input("Edad nueva: "))
                personas[nombre] = edad
        elif opc == 5:
            print(personas)
        
        opc = func.mostrar_menu()
