#import funciones as f
from funciones import *
import sys

argumentos = sys.argv
figuras = {}

if len(argumentos) > 1:
    crear_figuras_defecto(figuras)
    figura = argumentos[1]
    dibujar_una_figura(figuras, figura)
else:
    MENU = """      
            MENU    
        ==========
        1. Cargar figuras por defecto
        2. Crear una nueva figura desde cero
        3. Dibujar un polígono 
        4. Dibujar todos los polígonos 
        
        9. Salir
        """

    print(MENU)

    opcion = int(input("> "))
    while opcion != 9:
        if opcion == 1:
           crear_figuras_defecto(figuras)
        elif opcion == 2:
            crear_nueva_figura(figuras)  
        elif opcion == 3:
            figura = input("Figura a pintar: ")
            dibujar_una_figura(figuras, figura) 
        elif opcion == 4:
            dibujar_figuras(figuras)
        elif opcion == 9:
            print("Bye")
        
        print(MENU)
        opcion = int(input("> "))