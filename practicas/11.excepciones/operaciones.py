import matplotlib.pyplot as plt
from excepciones import *
from constantes import *

def mostrar_menu()->None:
    """
    Raises: 
        OpcionNoValidaError
    """
    print("""
        1.- Crear persona
        2.- Cargar personas por defecto de un fichero
        3.- Mostrar todas las personas
        4.- Mostrar personas de una ciudad
        5.- Dibujar histograma por ciudades
        6.- Salir y guardar en un fichero
        """)

    opcion_str = input(">>> ")
    try:
        opcion = int(opcion_str)
        if opcion < 1 or opcion > 6:
            raise OpcionNoValidaError("La opción debe estar entre 1 y 6")
    except ValueError as _:
        raise OpcionNoValidaError("Introduce un número")

    return opcion

def crear_personas(personas_dict:dict)->None:
    nombre = input("Nombre: ")
    if nombre != nombre.capitalize():
        raise NombreError(f"El nombre debería tener el suguiente formato: {nombre.capitalize()}")
    
    dni = input("DNI: ")
    if not is_dni_valido(dni):
        raise DNIError(f"El DNI no es válido")
    
    ciudad = input("Ciudad: ")
    if ciudad in personas_dict:
        personas = personas_dict[ciudad]  
        personas.append((nombre, dni))
    else:
        personas = []
        personas.append((nombre, dni))
        personas_dict[ciudad] = personas 

def is_dni_valido(dni:str)->bool:
    try:
        numero_str = dni[:-1]  # "11"
        suma = int(numero_str[0]) + int(numero_str[1]) 
        letra = dni[-1:]  # "C"
        return letra == chr(65 + suma) and letra.isupper() and letra.isalpha()
    except:  # Se pueden lanzar varias excepciones
        return False

def cargar_personas_por_defecto(source:int = LEER_DICCIONARIO_POR_DEFECTO):
    if source == LEER_DICCIONARIO_POR_DEFECTO:
        ascii_letra_inicio = 65
        personas_dict = {
                            "Madrid": [
                                        ("Luis", "11"+chr(ascii_letra_inicio+2)),
                                        ("Ana", "22"+chr(ascii_letra_inicio+4)),
                                        ("María", "33"+chr(ascii_letra_inicio+6))
                                    ],
                            "Barcelona": [
                                        ("Javier", "44"+chr(ascii_letra_inicio+8)),
                                        ("Julián", "66"+chr(ascii_letra_inicio+12))
                                        ],
                            "Bilbao": [
                                        ("Raquel", "77"+chr(ascii_letra_inicio+14))
                                    ]
                            }
    else:
        with open("personas_defecto.txt", "r", encoding="utf-8") as fichero:
            personas_dict = {}
            for linea in fichero:
                ciudad, nombre, dni = linea.split(", ")
                ciudad = ciudad.strip()
                nombre = nombre.strip()
                dni = dni.strip()
                if ciudad in personas_dict:
                    personas_dict[ciudad].append((nombre, dni))
                else:
                    personas_dict[ciudad] = [(nombre, dni)]

    return personas_dict

def mostrar_todas_personas(personas_dict:dict):
    for ciudad, personas in personas_dict.items():
        print(ciudad)
        print("-------")
        output_personas(personas)

def mostrar_personas_ciudad(personas_dict:dict):
    ciudad = input("Introduce ciudad: ")
    if ciudad in personas_dict:
        personas = personas_dict[ciudad]
        output_personas(personas)
    else:
        print("La ciudad no existe")

def output_personas(personas):
    for persona in personas:
        nombre, dni = persona
        print(f" ·  {nombre} - {dni}")

def dibujar_histograma(personas_dict:dict):
    ys = []
    xs = personas_dict.keys()
    for personas in xs:
        ys.append(len(personas_dict[personas]))

    plt.title("Histograma de personas por ciudad")
    plt.bar(xs, ys)
    plt.yticks(range(0, max(ys)+1))

    plt.show()

def guardar_diccionario(personas_dict:dict):
    with open("personas.csv", "a", encoding="utf-8") as fichero_csv:
        for persona, lista_personas in personas_dict.items():
            for nombre, dni in lista_personas: 
                fichero_csv.write(f"{persona}, {nombre}, {dni}\n")
