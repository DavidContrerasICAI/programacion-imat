import operaciones as op
from excepciones import OpcionNoValidaError, NombreError, DNIError

if __name__ == "__main__":
    opcion = 0
    while opcion != 6:
        opcion_valida = False
        while not opcion_valida:
            try:
                opcion = op.mostrar_menu()
                opcion_valida = True
            except OpcionNoValidaError as error:
                print(error)
        
        if opcion == 1:
            try:
                op.crear_personas()
            except NombreError as error:
                print("··E001··", error)
            except DNIError as error:
                print("··E002··", error)
        elif opcion == 2:
            op.cargar_personas_por_defecto()
        elif opcion == 3:
            op.mostrar_todas_personas()
        elif opcion == 4:
            op.mostrar_personas_ciudad()
        elif opcion == 5:
            op.dibujar_histograma()

