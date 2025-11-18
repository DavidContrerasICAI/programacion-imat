class Persona:
    def __init__(self, nombre:str, edad:int, ciudad:str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self) -> str:
        return f"{self.nombre} ({self.edad}) - {self.ciudad}"


lista_fichero = []
with open("personas.txt", "r") as fichero:
    lista_fichero = fichero.readlines()

print(lista_fichero)

personas = []
i = 0
while i < len(lista_fichero):
    nombre = lista_fichero[i].rstrip()
    edad = int(lista_fichero[i+1].rstrip())
    ciudad = lista_fichero[i+2].rstrip()

    personas.append(Persona(nombre, edad, ciudad))

    i += 3

for persona in personas:
    print(persona)

