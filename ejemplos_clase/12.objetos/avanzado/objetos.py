from excepciones import *

class Persona:
    def __init__(self, nombre:str, edad:int):
        """
        self.nombre = "Luis"    # Atributo
        nombre = "Luis"    # Variable local
        """
        self.nombre = nombre
        if edad > 0 and edad < 100:
            self.edad = edad
        else:
            raise EdadError(f"La edad {edad} de {nombre} no está entre 1 y 99 años")

    def cumpleanios(self):
        if self.edad < 99:
            self.edad += 1
        else:
            raise EdadError(f"La edad de {self.nombre} no puede ser mayor de 99 años")

    def __str__(self):
        return f"{self.nombre} ({self.edad})"
