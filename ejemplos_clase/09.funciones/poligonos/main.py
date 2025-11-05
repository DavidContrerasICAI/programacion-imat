import matplotlib.pyplot as plt
import sys

def crear_figuras_defecto(figuras:dict):
    figuras["pentagono"] = [(1,1), (3,1), (4,2), (2,3), (0,2), (1,1)]
    figuras["triangulo"] = [(2,2), (2,4), (5,5), (2,2)]
    print("2 figuras cargadas...")

def crear_nueva_figura(figuras:dict):
    figura = input("Introduzca un nombre de figura: ")
    puntos = []
    punto = input("Introduzca el primer punto x,y (Z para terminar): ")
    while punto.upper() != "Z":
        coma = punto.index(",")
        x, y = punto[:coma], punto[coma+1:]
        x = int(x.strip())
        y = int(y.strip())
        puntos.append((x, y))
        punto = input("Siguiente punto x, y (Z para terminar): ")
    
    puntos.append(puntos[0])
    figuras[figura] = puntos

def dibujar_una_figura(figuras:dict, figura:str = None):
    xs = []
    ys = []
    if figura == None:
        figura = input("Figura a pintar: ")
    if figura in figuras:
        puntos = figuras[figura]
        for x, y in puntos:
            xs.append(x)
            ys.append(y)

        plt.figure()
        plt.plot(xs,ys) 
        plt.show()
    else:
        print("Figura no encontrada") 

def dibujar_figuras(figuras:dict):
    plt.figure()
    for puntos in figuras.values():
        xs = []
        ys = []
        for x, y in puntos:
            xs.append(x)
            ys.append(y)
        
        plt.plot(xs,ys) 
    
    plt.show()

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
            dibujar_una_figura(figuras) 
        elif opcion == 4:
            dibujar_figuras(figuras)
        elif opcion == 9:
            print("Bye")
        
        print(MENU)
        opcion = int(input("> "))