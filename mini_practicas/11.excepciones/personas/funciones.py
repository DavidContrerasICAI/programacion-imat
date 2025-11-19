def crear_persona(informacion:str) -> tuple[str, int]:
    """
    Extrae el nombre y edad de una persona a partir de un string con los siguientes criterios:
        - El nombre entre 4 y 10 caracteres y capitalizada
        - La edad con un valor entre 18 y 99
    
    Args:
        informacion: contiene en un string el nombre y edad

    Returns:
        (nombre:str, edad:int)

    Raises:
        ValueError: si no se puede crear la Persona
    """

    try:
        nombre, edad = informacion.split(",")
        nombre = nombre.strip()
        edad = edad.strip()
        edad = int(edad)
    except ValueError:
        raise ValueError(f"La edad {edad} no es un número")
    
    if not (len(nombre) >= 4 and len(nombre) <= 10):
        raise ValueError("La longitud del nombre debe estar entre 4 y 10 caracteres")
    
    if not (nombre[0].upper() == nombre[0]):
        raise ValueError("El nombre debe empezar por mayúsculas")
    
    if not (edad >= 18 and edad <= 99):
        raise ValueError("La edad debe estar comprendida entre 18 y 99 años")

    return (nombre, edad)