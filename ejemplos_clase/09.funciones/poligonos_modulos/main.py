import funciones as func

if __name__ == "__main__":
    MENU = """      
            MENU    
        ==========
        1. Cargar figuras por defecto
        2. Crear una nueva figura desde cero
        3. Dibujar un polígono 
        4. Dibujar todos los polígonos 
        
        9. Salir
        """

    figuras = {}

    print(MENU)
    opcion = int(input("> "))
    while opcion != 9:
        if opcion == 1:
            func.crear_figuras_por_defecto(figuras)
        elif opcion == 2:
            func.crear_figura(figuras)
        elif opcion == 3:
            func.pintar_figura(figuras)
        elif opcion == 4:
            func.pintar_figuras(figuras)
        elif opcion == 9:
            print("Bye")
        
        print(MENU)
        opcion = int(input("> "))