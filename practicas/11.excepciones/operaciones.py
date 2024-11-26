import matplotlib.pyplot as plt
from excepciones import *

personas_dict = dict()

def mostrar_menu():
    """
    Raises: 
        OpcionNoValidaError
    """
    print("""
        1.- Crear persona
        2.- Cargar personas por defecto
        3.- Mostrar todas las personas
        4.- Mostrar personas de una ciudad
        5.- Dibujar histograma por ciudades
        6.- Salir
        """)

    opcion_str = input(">>> ")
    try:
        opcion = int(opcion_str)
        if opcion < 1 or opcion > 6:
            raise OpcionNoValidaError("La opción debe estar entre 1 y 6")
    except ValueError as error:
        raise OpcionNoValidaError("Introduce un número")

    return opcion

def crear_personas():
    global personas_dict
    
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

def is_dni_valido(dni):
    try:
        numero_str = dni[:-1]  # "11"
        suma = int(numero_str[0]) + int(numero_str[1]) 
        letra = dni[-1:]  # "C"
        return letra == chr(65 + suma) and letra.isupper() and letra.isalpha()
    except:  # Se pueden lanzar varias excepciones
        return False

def cargar_personas_por_defecto():
    global personas_dict
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

def mostrar_todas_personas():
    for ciudad, personas in personas_dict.items():
        print(ciudad)
        print("-------")
        output_personas(personas)

def mostrar_personas_ciudad():
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

def dibujar_histograma():
    ys = []
    xs = personas_dict.keys()
    for personas in xs:
        ys.append(len(personas_dict[personas]))

    plt.title("Histograma de personas por ciudad")
    plt.bar(xs, ys)
    plt.yticks(range(0, max(ys)+1))

    plt.show()