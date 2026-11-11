import matplotlib.pyplot as plt

def sumar(a:int, b:int) -> int:
    suma = a + b
    return suma

suma = sumar(3, 5)
print(suma)


def crear_figuras_por_defecto():
    figuras["pentagono"] = [(1,1), (3,1), (4,2), (2,3), (0,2), (1,1)]
    figuras["triangulo"] = [(2,2), (2,4), (5,5), (2,2)]
    print("2 figuras cargadas...")


def crear_figura():
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


def pintar_figura():
    xs = []
    ys = []
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


def dibujar_todas_figuras():
    plt.figure()
    for puntos in figuras.values():
        xs = []
        ys = []
        for x, y in puntos:
            xs.append(x)
            ys.append(y)
        
        plt.plot(xs,ys) 
    
    plt.show()

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

figuras = dict()


opcion = int(input("> "))
while opcion != 9:
    if opcion == 1:
        crear_figuras_por_defecto()
    elif opcion == 2:
        crear_figura()
    elif opcion == 3:
        pintar_figura()
    elif opcion == 4:
        dibujar_todas_figuras()
    elif opcion == 9:
        print("Bye")
    
    print(MENU)
    opcion = int(input("> "))