from constantes import *
from excepciones import CoordenadasError
import objetos as obj
import funciones as func
import time

if __name__ == "__main__":
    matriz = []

    print("\n\n### Leyenda:\n")
    print(f"{COLOR_AMARILLO+CHAR_CLIENTE+COLOR_DEFECTO}: Cliente de Uber")
    print(f"{COLOR_VERDE+CHAR_UBER+COLOR_DEFECTO}: Uber libre, no tiene servicio")
    print(f"{COLOR_AZUL+CHAR_UBER+COLOR_DEFECTO}: Uber buscando cliente")
    print(f"{COLOR_ROJO+CHAR_UBER+COLOR_DEFECTO}: Uber llevando cliente")

    print("\n### Creando ciudad...\n")
    func.init_ciudad(matriz)
    func.print_ciudad(matriz)

    # Crear objetos
    clientes:list[obj.Cliente] = []
    ubers:list[obj.Vehiculo] = []
    
    coordenadas_ubers = [(0, 2), (4, 4)]
    coordenadas_clientes = [(3, 0), (4, 2)]
    nombres_clientes = ["Luis", "Ana"]

    for x, y in coordenadas_ubers:
        uber = obj.Vehiculo(x, y)
        func.posicionar_en_ciudad(matriz, uber)
        ubers.append(uber)

    index = 0
    for x, y in coordenadas_clientes:
        cliente = obj.Cliente(nombres_clientes[index], x, y)
        func.posicionar_en_ciudad(matriz, cliente)
        clientes.append(cliente)
        index += 1

    print("### Posicionando objetos...\n")
    func.print_ciudad(matriz)

    # Asignación de los destinos

    numero = 1
    for cliente in clientes:
        error = True
        while error:
            try:
                coordenadas_destino_str = input(f"Introduzca el destino del cliente #{numero} (x,y): ")
                x, y = func.parsear_destino(coordenadas_destino_str)
                cliente.set_destino(x, y)
                error = False
            except CoordenadasError as err:
                print(err)
        numero += 1

    # Asignación de clientes a ubers: uno a uno

    for i in range(len(clientes)):
        ubers[i].cliente = clientes[i] 


    # Simulación

    print("\n### Ubers en marcha...\n")
    ubers_in_movimiento = True
    while ubers_in_movimiento:
        ubers_in_movimiento = False
        for uber in ubers:
            uber.mover(matriz)
            if uber.isMovimiento():
                ubers_in_movimiento = True

            print(uber)

        func.print_ciudad(matriz)
        time.sleep(0.5)


    print("\n### Fin de la simulación")