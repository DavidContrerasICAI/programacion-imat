def procesar(nombre:str, edad:int)->str:
    nombre = nombre.upper()
    if len(nombre) >= 3:
        nombre = nombre[:3]
    resultado = nombre + str(edad)
    # Muy mala práctica: return resultado, True, [1, 2, 3]
    return resultado

def crear_persona(nombre:str, edad:int, direccion:str):
    nombre_limpio = nombre.strip().upper()
    ok = True
    if len(nombre) >= 4:
        nombre = nombre[:4]
        if direccion.startswith("C\\") and direccion.endswith("38"):
            return (nombre_limpio, edad, direccion)
        else:
            return None
    else:
        return None

nombre = "Lu"
edad = 22
nombre_completo = procesar(nombre, 33)
print(nombre_completo)

nombre = "Luis"
edad = 22
nombre_completo = procesar(nombre, 33)
print(nombre_completo)

persona = crear_persona(nombre, 22, "C\ del pez, 38")
if persona != None:
    print(persona)
else:
    print("Error")

persona = crear_persona(nombre, 22, "del pez, 38")
if persona != None:
    print(persona)
else:
    print("Error")