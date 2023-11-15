import funciones as f

if __name__ == "__main__":
    f.mostrar_menu()

    opcion = int(input("> "))
    while opcion != 9:
        if opcion == 1:
            f.cargar_figuras()
        elif opcion == 2:
            f.crear_figura()
        elif opcion == 3:
            f.pintar_figura()
        elif opcion == 4:
            f.pintar_figuras()
        elif opcion == 9:
            print("Bye")
        
        f.mostrar_menu()
        opcion = int(input("> "))