# https://pythontutor.com/visualize.html#mode=edit

a = 1
b = 2
s = "hola"
lista = []

def sumar(a:int, b:int) -> int:
    """
    Suma rara de dos números
    """
    a += 1
    s = "Adios"
    print("Variable a en sumar (local):", a)
    suma_ejemplo = a + b
    return suma_ejemplo


def gestionar_lista(opcion:int, valor:str)-> None:
    if opcion == 1:
        lista.append(valor)
    elif opcion == 2 and valor in lista:
        lista.remove(valor)
    elif opcion == 3:
        lista.insert(0, valor)

suma = sumar(a, b)
print("Variable a en main (global):", a)
print("Variable s en main (global):", s)
print("Resultado de suma rara:", suma)

gestionar_lista(1, "Uno")
gestionar_lista(1, "Dos")
gestionar_lista(1, "Tres")

gestionar_lista(2, "Dos")

gestionar_lista(3, "Cero")

print(lista)

print("Esta línea dará error, por eso está la última:", suma_ejemplo)