class Alumno:
    def __init__(self, nombre, clave, curso):
        self.nombre = nombre
        self.clave = clave
        self.curso = curso

    def __str__(self) -> str:
        return f"{self.nombre} ({self.clave}) - {self.curso}"


class Asignatura:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self) -> str:
        return f"{self.nombre}: {self.nota}"